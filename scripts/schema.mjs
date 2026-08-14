// Creates the pgvector extension and the chunks table.
// Run once: `node scripts/schema.mjs`
import { sql } from '@vercel/postgres';

// text-embedding-3-small = 1536 dims. If you switch embedding models, change DIM
// here AND in ingest.mjs, then re-ingest.
const DIM = 1536;

async function main() {
  await sql`CREATE EXTENSION IF NOT EXISTS vector;`;

  await sql.query(`
    CREATE TABLE IF NOT EXISTS chunks (
      id          BIGSERIAL PRIMARY KEY,
      url         TEXT NOT NULL,
      title       TEXT,
      chunk_index INT  NOT NULL,
      content     TEXT NOT NULL,
      embedding   vector(${DIM}) NOT NULL,
      UNIQUE (url, chunk_index)
    );
  `);

  // Approximate-nearest-neighbour index. ivfflat needs data to train on; it's fine
  // to create it now and it'll be used once rows exist. Cosine distance.
  await sql.query(`
    CREATE INDEX IF NOT EXISTS chunks_embedding_idx
    ON chunks USING ivfflat (embedding vector_cosine_ops) WITH (lists = 100);
  `);

  console.log('Schema ready.');
  process.exit(0);
}

main().catch((e) => { console.error(e); process.exit(1); });
