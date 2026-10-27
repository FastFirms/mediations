/**
 * scripts/mediator-eoi-schema.mjs
 *
 * Creates the mediator-network expression-of-interest tables in Neon.
 * Run once with: node scripts/mediator-eoi-schema.mjs  (needs POSTGRES_URL)
 * Safe to re-run — CREATE ... IF NOT EXISTS.
 *
 * Deliberately separate from the client enquiry tables: recruitment records
 * never enter client intake queues, Access Mediation or chatbot lead feeds.
 */

import { sql } from '@vercel/postgres';

async function run() {
  await sql`
    CREATE TABLE IF NOT EXISTS mediator_eois (
      id                    BIGSERIAL PRIMARY KEY,
      submission_id         UUID NOT NULL UNIQUE,
      submitted_at          TIMESTAMPTZ NOT NULL DEFAULT NOW(),
      source                TEXT NOT NULL DEFAULT 'mediator_network_eoi',
      form_version          TEXT NOT NULL,
      name                  TEXT NOT NULL,
      email                 TEXT NOT NULL,
      phone                 TEXT NOT NULL,
      city                  TEXT NOT NULL,
      state                 TEXT NOT NULL,
      organisation          TEXT,
      website               TEXT,
      practice_type         TEXT,
      credential_types      TEXT[] NOT NULL,
      credential_body       TEXT,
      credential_identifier TEXT,
      experience_band       TEXT NOT NULL,
      practice_areas        TEXT[] NOT NULL,
      regions_served        TEXT NOT NULL,
      delivery_modes        TEXT[] NOT NULL,
      venue_access          TEXT,
      capacity_band         TEXT,
      languages             TEXT,
      background            TEXT,
      motivation            TEXT,
      accuracy_confirmed    BOOLEAN NOT NULL,
      privacy_acknowledged  BOOLEAN NOT NULL,
      consent_version       TEXT NOT NULL,
      consent_at            TIMESTAMPTZ NOT NULL DEFAULT NOW(),
      marketing_opt_in      BOOLEAN NOT NULL DEFAULT FALSE,
      review_status         TEXT NOT NULL DEFAULT 'NEW' CHECK (review_status IN (
                              'NEW','IN_REVIEW','MORE_INFORMATION_REQUESTED',
                              'DISCUSSION_INVITED','APPROVED_FOR_ONBOARDING','NOT_PROCEEDING')),
      assigned_reviewer     TEXT,
      reviewed_at           TIMESTAMPTZ,
      internal_notes        TEXT,
      notification_status   TEXT NOT NULL DEFAULT 'PENDING' CHECK (notification_status IN ('PENDING','SENT','FAILED')),
      notification_attempts INT NOT NULL DEFAULT 0
    )
  `;
  await sql`CREATE INDEX IF NOT EXISTS mediator_eois_status_idx ON mediator_eois (review_status, submitted_at DESC)`;
  await sql`CREATE INDEX IF NOT EXISTS mediator_eois_email_idx ON mediator_eois (lower(email), submitted_at DESC)`;

  await sql`
    CREATE TABLE IF NOT EXISTS mediator_eoi_audit_log (
      id            BIGSERIAL PRIMARY KEY,
      submission_id UUID,
      event_type    TEXT NOT NULL,
      actor         TEXT,
      detail        TEXT,
      created_at    TIMESTAMPTZ NOT NULL DEFAULT NOW()
    )
  `;
  await sql`CREATE INDEX IF NOT EXISTS mediator_eoi_audit_actor_idx ON mediator_eoi_audit_log (event_type, actor, created_at DESC)`;

  console.log('mediator_eois + mediator_eoi_audit_log ready');
}

run().catch(err => { console.error(err.message); process.exit(1); });
