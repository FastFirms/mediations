/**
 * Access Mediation database schema.
 * Run once: node --env-file=.env.local scripts/access-schema.mjs
 *
 * Tables:
 *   access_matters       — shared matter record (non-financial)
 *   access_assessments   — per-participant financial assessment (private)
 *   access_applications  — Party A application details + other-party contact
 *   access_capacity      — monthly capacity ledger (units consumed per booking)
 *   access_audit_log     — immutable audit trail for overrides and status changes
 *
 * Design principles (from build pack):
 *   - Financial assessments belong to the participant, not the shared matter.
 *   - access_assessments has stricter access controls than general matter data.
 *   - Sensitive financial data is stored as bands (never exact figures).
 *   - Internal targets / subsidy calculations are computed at reporting time,
 *     not stored as denormalised columns.
 *   - Capacity is consumed at booking, not at application time.
 */
import { sql } from '@vercel/postgres';

async function main() {
  console.log('Creating Access Mediation schema…');

  // ── Sequence for human-readable matter IDs ──────────────────────────────
  await sql`CREATE SEQUENCE IF NOT EXISTS access_matter_seq START 1;`;

  // ── access_matters ───────────────────────────────────────────────────────
  // Shared matter record. Only non-financial shared state lives here.
  // Party A / B contribution status is a summary only; detailed assessments
  // are in access_assessments (separate, restricted).
  await sql`
    CREATE TABLE IF NOT EXISTS access_matters (
      matter_id              TEXT PRIMARY KEY,
      created_at             TIMESTAMPTZ NOT NULL DEFAULT now(),
      updated_at             TIMESTAMPTZ NOT NULL DEFAULT now(),

      status                 TEXT NOT NULL DEFAULT 'NEW'
                               CHECK (status IN (
                                 'NEW','AUTO_ELIGIBLE','REVIEW_REQUIRED','APPROVED',
                                 'STANDARD_FEE','WAITLISTED','DECLINED_ACCESS',
                                 'INTAKE','READY_TO_BOOK','BOOKED','COMPLETED','CANCELLED'
                               )),
      matter_type            TEXT,

      -- Service duration is confirmed by staff after intake, not by calculator alone
      service_duration_minutes INTEGER DEFAULT 180
                               CHECK (service_duration_minutes IN (180, 360)),

      -- Capacity is set when the appointment is formally booked
      capacity_units         NUMERIC(3,1),
      capacity_month         TEXT,

      -- Summary contribution status (details stay in access_assessments)
      party_a_status         TEXT DEFAULT 'PENDING',
      party_b_status         TEXT DEFAULT 'PENDING',
      combined_revenue_ex_gst INTEGER,

      -- Invitation tracking
      invitation_sent_at     TIMESTAMPTZ,
      invitation_expires_at  TIMESTAMPTZ,
      invitation_token       TEXT UNIQUE,

      internal_notes         TEXT
    );
  `;

  // ── access_assessments ───────────────────────────────────────────────────
  // Per-participant financial assessment. Private between that participant and
  // authorised admin — never exposed to the other participant.
  await sql`
    CREATE TABLE IF NOT EXISTS access_assessments (
      assessment_id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
      matter_id                  TEXT REFERENCES access_matters(matter_id),
      participant_role           TEXT NOT NULL CHECK (participant_role IN ('party_a','party_b')),
      created_at                 TIMESTAMPTZ NOT NULL DEFAULT now(),
      updated_at                 TIMESTAMPTZ NOT NULL DEFAULT now(),

      -- Contact
      participant_name           TEXT,
      participant_email          TEXT,
      participant_phone          TEXT,
      preferred_contact          TEXT,

      -- Calculator inputs stored as bands, never exact figures
      income_band                TEXT,
      dependants_band            TEXT,
      assets_band                TEXT,
      assets_accessible          BOOLEAN,
      concession_status          TEXT,
      hardship_category          TEXT,
      needs_60i                  TEXT,
      matter_type_declared       TEXT,

      -- Calculator outputs
      calculated_band            INTEGER,
      calculated_contribution_ex_gst INTEGER,
      result_type                TEXT,
      review_flags               TEXT[],
      calculator_version         TEXT DEFAULT '1.0',

      -- Admin approval
      approval_status            TEXT NOT NULL DEFAULT 'NEW'
                                   CHECK (approval_status IN (
                                     'NEW','AUTO_ELIGIBLE','REVIEW_REQUIRED',
                                     'APPROVED','STANDARD_FEE','WAITLISTED',
                                     'DECLINED_ACCESS'
                                   )),
      approved_contribution_ex_gst INTEGER,
      approved_band              INTEGER,
      approved_by                TEXT,
      approved_at                TIMESTAMPTZ,
      override_reason_code       TEXT,

      -- Fee confirmation
      confirmed_contribution_ex_gst INTEGER,
      fee_confirmed_at           TIMESTAMPTZ,

      -- Assessment validity (90 days for follow-up reuse — spec §118)
      assessment_valid_until     TIMESTAMPTZ,

      -- Consent (required before application is accepted)
      privacy_consent            BOOLEAN NOT NULL DEFAULT false,
      accuracy_declaration       BOOLEAN NOT NULL DEFAULT false
    );
  `;

  // ── access_applications ──────────────────────────────────────────────────
  // Party A application: contact info, other-party details, notification state.
  await sql`
    CREATE TABLE IF NOT EXISTS access_applications (
      application_id         UUID PRIMARY KEY DEFAULT gen_random_uuid(),
      matter_id              TEXT REFERENCES access_matters(matter_id),
      assessment_id          UUID REFERENCES access_assessments(assessment_id),
      created_at             TIMESTAMPTZ NOT NULL DEFAULT now(),

      -- Party A contact
      party_a_name           TEXT NOT NULL,
      party_a_email          TEXT NOT NULL,
      party_a_phone          TEXT,

      -- Other party (for invitation workflow)
      other_party_name       TEXT,
      other_party_email      TEXT,
      other_party_phone      TEXT,
      relationship_to_other  TEXT,
      lawyer_name            TEXT,
      lawyer_email           TEXT,

      matter_type            TEXT,
      preferred_timing       TEXT,

      -- Formspree notification audit (staff alert only, no financial data in payload)
      notification_sent_at   TIMESTAMPTZ,
      notification_ref       TEXT,
      notification_error     TEXT
    );
  `;

  // ── access_capacity ──────────────────────────────────────────────────────
  // Monthly capacity ledger. Capacity is consumed at booking, not application.
  // 3h = 1 unit, 6h = 2 units, 90-min follow-up = 0.5 units. Limit = 8/month.
  await sql`
    CREATE TABLE IF NOT EXISTS access_capacity (
      capacity_id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
      capacity_month         TEXT NOT NULL,
      matter_id              TEXT REFERENCES access_matters(matter_id),
      units_consumed         NUMERIC(3,1) NOT NULL CHECK (units_consumed > 0),
      status                 TEXT NOT NULL DEFAULT 'ACTIVE'
                               CHECK (status IN (
                                 'ACTIVE','RELEASED','LOST_ACCESS_CAPACITY',
                                 'PRACTITIONER_CANCELLED'
                               )),
      created_at             TIMESTAMPTZ NOT NULL DEFAULT now(),
      released_at            TIMESTAMPTZ,
      release_reason         TEXT,
      notes                  TEXT
    );
  `;

  // ── access_audit_log ─────────────────────────────────────────────────────
  // Immutable append-only audit trail. Every status change, override and
  // staff action is recorded with a reason code.
  await sql`
    CREATE TABLE IF NOT EXISTS access_audit_log (
      log_id                 UUID PRIMARY KEY DEFAULT gen_random_uuid(),
      created_at             TIMESTAMPTZ NOT NULL DEFAULT now(),
      matter_id              TEXT,
      assessment_id          UUID,
      action                 TEXT NOT NULL,
      actor                  TEXT,
      old_value              JSONB,
      new_value              JSONB,
      reason_code            TEXT,
      notes                  TEXT
    );
  `;

  // ── Indexes ──────────────────────────────────────────────────────────────
  await sql`CREATE INDEX IF NOT EXISTS idx_am_status
    ON access_matters (status, created_at DESC);`;
  await sql`CREATE INDEX IF NOT EXISTS idx_aa_matter
    ON access_assessments (matter_id);`;
  await sql`CREATE INDEX IF NOT EXISTS idx_aa_email
    ON access_assessments (participant_email);`;
  await sql`CREATE INDEX IF NOT EXISTS idx_aa_approval
    ON access_assessments (approval_status);`;
  await sql`CREATE INDEX IF NOT EXISTS idx_aapp_matter
    ON access_applications (matter_id);`;
  await sql`CREATE INDEX IF NOT EXISTS idx_cap_month
    ON access_capacity (capacity_month) WHERE status = 'ACTIVE';`;
  await sql`CREATE INDEX IF NOT EXISTS idx_audit_matter
    ON access_audit_log (matter_id, created_at DESC);`;

  console.log('Access Mediation schema ready.');
  process.exit(0);
}

main().catch((e) => { console.error(e); process.exit(1); });
