/**
 * scripts/enquiry-schema.mjs
 *
 * Database migration: create enquiry tables in Neon.
 * Run once with: node scripts/enquiry-schema.mjs
 *
 * Requires POSTGRES_URL in environment (from .env.local or Vercel env pull).
 * Safe to re-run — uses CREATE TABLE IF NOT EXISTS.
 *
 * Tables created:
 *   enquiries              — routing result and non-sensitive submission data
 *   enquiry_contacts       — restricted: name, email, phone, message
 *   enquiry_branch_answers — branch-specific question answers
 *   enquiry_audit_log      — event log (rate limiting, overrides, status changes)
 */

import { sql } from '@vercel/postgres';

async function run() {
  console.log('Creating enquiry tables...');

  await sql`
    CREATE TABLE IF NOT EXISTS enquiries (
      id                            BIGSERIAL PRIMARY KEY,
      submission_id                 UUID NOT NULL UNIQUE DEFAULT gen_random_uuid(),
      form_variant                  TEXT NOT NULL CHECK (form_variant IN ('guided','quick')),
      schema_version                TEXT NOT NULL DEFAULT '1.0',
      routing_rules_version         TEXT NOT NULL,
      submitted_at                  TIMESTAMPTZ NOT NULL DEFAULT NOW(),
      matter_category               TEXT,
      stage                         TEXT,
      desired_outcome               TEXT,
      party_b_status                TEXT,
      enquirer_role                 TEXT,
      delivery_preference           TEXT,
      state                         TEXT,
      city                          TEXT,
      timing                        TEXT,
      fee_preference                TEXT,
      operational_queue             TEXT NOT NULL,
      professional_review_required  BOOLEAN NOT NULL DEFAULT FALSE,
      review_reasons                TEXT[] NOT NULL DEFAULT '{}',
      tags                          TEXT[] NOT NULL DEFAULT '{}',
      safe_email                    BOOLEAN,
      safe_voicemail                BOOLEAN,
      safe_phone                    BOOLEAN,
      preferred_contact_time        TEXT,
      safety_flag                   TEXT,
      attribution_landing           TEXT,
      attribution_referrer          TEXT,
      attribution_utm_source        TEXT,
      attribution_utm_medium        TEXT,
      attribution_utm_campaign      TEXT,
      consent_version               TEXT,
      privacy_consent               BOOLEAN NOT NULL DEFAULT FALSE,
      accuracy_declaration          BOOLEAN NOT NULL DEFAULT FALSE,
      formspree_notified            BOOLEAN NOT NULL DEFAULT FALSE,
      notification_attempts         INTEGER NOT NULL DEFAULT 0,
      notification_last_error       TEXT,
      created_at                    TIMESTAMPTZ NOT NULL DEFAULT NOW()
    )
  `;
  console.log('  ✓ enquiries');

  await sql`
    CREATE TABLE IF NOT EXISTS enquiry_contacts (
      id                      BIGSERIAL PRIMARY KEY,
      enquiry_submission_id   UUID NOT NULL REFERENCES enquiries(submission_id) ON DELETE CASCADE,
      name                    TEXT,
      email                   TEXT,
      phone                   TEXT,
      message                 TEXT,
      created_at              TIMESTAMPTZ NOT NULL DEFAULT NOW()
    )
  `;
  console.log('  ✓ enquiry_contacts');

  await sql`
    CREATE TABLE IF NOT EXISTS enquiry_branch_answers (
      id                      BIGSERIAL PRIMARY KEY,
      enquiry_submission_id   UUID NOT NULL REFERENCES enquiries(submission_id) ON DELETE CASCADE,
      answer_key              TEXT NOT NULL,
      answer_value            TEXT NOT NULL,
      created_at              TIMESTAMPTZ NOT NULL DEFAULT NOW()
    )
  `;
  console.log('  ✓ enquiry_branch_answers');

  await sql`
    CREATE TABLE IF NOT EXISTS enquiry_audit_log (
      id                      BIGSERIAL PRIMARY KEY,
      enquiry_submission_id   UUID REFERENCES enquiries(submission_id) ON DELETE SET NULL,
      event_type              TEXT NOT NULL,
      actor                   TEXT,
      reason                  TEXT,
      created_at              TIMESTAMPTZ NOT NULL DEFAULT NOW()
    )
  `;
  console.log('  ✓ enquiry_audit_log');

  // Stage C/D column additions (ADD COLUMN IF NOT EXISTS is idempotent)
  await sql`ALTER TABLE enquiries ADD COLUMN IF NOT EXISTS formspree_notified BOOLEAN NOT NULL DEFAULT FALSE`;
  await sql`ALTER TABLE enquiries ADD COLUMN IF NOT EXISTS notification_attempts INTEGER NOT NULL DEFAULT 0`;
  await sql`ALTER TABLE enquiries ADD COLUMN IF NOT EXISTS notification_last_error TEXT`;
  console.log('  ✓ stage-c/d columns');

  // MA-OPS-003: Farley receipt acknowledgement
  await sql`ALTER TABLE enquiries ADD COLUMN IF NOT EXISTS acknowledged_at TIMESTAMPTZ`;
  await sql`ALTER TABLE enquiries ADD COLUMN IF NOT EXISTS acknowledged_via VARCHAR(32)`;
  await sql`ALTER TABLE enquiries ADD COLUMN IF NOT EXISTS ack_user_agent TEXT`;
  await sql`CREATE INDEX IF NOT EXISTS idx_enquiries_unacked ON enquiries(submitted_at) WHERE acknowledged_at IS NULL`;
  console.log('  ✓ ma-ops-003 columns');

  // Indexes for common queries
  await sql`CREATE INDEX IF NOT EXISTS idx_enquiries_queue ON enquiries(operational_queue)`;
  await sql`CREATE INDEX IF NOT EXISTS idx_enquiries_submitted ON enquiries(submitted_at DESC)`;
  await sql`CREATE INDEX IF NOT EXISTS idx_enquiries_notified ON enquiries(formspree_notified) WHERE NOT formspree_notified`;
  await sql`CREATE INDEX IF NOT EXISTS idx_enquiry_contacts_sid ON enquiry_contacts(enquiry_submission_id)`;
  await sql`CREATE INDEX IF NOT EXISTS idx_enquiry_audit_actor ON enquiry_audit_log(actor, created_at)`;
  console.log('  ✓ indexes');

  console.log('\nMigration complete.');
  process.exit(0);
}

run().catch(err => { console.error(err); process.exit(1); });
