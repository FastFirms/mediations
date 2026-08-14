// Reads local site content JSON, chunks it, embeds each chunk, and upserts into Postgres.
// Run: `CONTENT_DIR=./content node scripts/ingest.mjs`
//
// >>> ADJUST loadDocuments() TO MATCH YOUR ACTUAL JSON SHAPE <<<
import fs from 'node:fs';
import path from 'node:path';
import { sql } from '@vercel/postgres';
import OpenAI from 'openai';

const openai = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });
const EMBED_MODEL = 'text-embedding-3-small'; // 1536 dims; matches schema.mjs
const CONTENT_DIR = process.env.CONTENT_DIR || './content';

// ~500 tokens ≈ ~2000 chars. Overlap keeps context across boundaries.
const CHUNK_CHARS = 2000;
const OVERLAP_CHARS = 200;

// ---------------------------------------------------------------------------
// Each .json file in CONTENT_DIR was produced by scripts/extract.mjs, which
// reads the built HTML pages and strips nav/footer/schema boilerplate.
// Shape: { "url": "https://...", "title": "...", "text": "...plain text..." }
// No further boilerplate stripping needed — extract.mjs already did it.
// ---------------------------------------------------------------------------
function loadDocuments() {
  const files = fs.readdirSync(CONTENT_DIR).filter((f) => f.endsWith('.json'));
  const docs = [];
  for (const f of files) {
    const it = JSON.parse(fs.readFileSync(path.join(CONTENT_DIR, f), 'utf8'));
    const { url, title = '', text = '' } = it;
    if (url && text.trim().length > 50) {
      docs.push({ url, title, text });
    }
  }
  return docs;
}

function chunk(text) {
  const out = [];
  let i = 0;
  while (i < text.length) {
    out.push(text.slice(i, i + CHUNK_CHARS));
    i += CHUNK_CHARS - OVERLAP_CHARS;
  }
  return out;
}

async function embedBatch(texts) {
  const res = await openai.embeddings.create({ model: EMBED_MODEL, input: texts });
  return res.data.map((d) => d.embedding);
}

const toVector = (arr) => `[${arr.join(',')}]`;

async function main() {
  const docs = loadDocuments();
  console.log(`Loaded ${docs.length} documents from ${CONTENT_DIR}`);
  if (docs.length === 0) {
    console.error('No documents. Check CONTENT_DIR and loadDocuments() mapping.');
    process.exit(1);
  }

  let total = 0;
  for (const doc of docs) {
    const parts = chunk(doc.text);
    // Embed in batches of 100 to stay under request limits.
    for (let start = 0; start < parts.length; start += 100) {
      const batch = parts.slice(start, start + 100);
      const embeddings = await embedBatch(batch);
      for (let j = 0; j < batch.length; j++) {
        const chunkIndex = start + j;
        await sql.query(
          `INSERT INTO chunks (url, title, chunk_index, content, embedding)
           VALUES ($1, $2, $3, $4, $5)
           ON CONFLICT (url, chunk_index)
           DO UPDATE SET title = EXCLUDED.title,
                         content = EXCLUDED.content,
                         embedding = EXCLUDED.embedding;`,
          [doc.url, doc.title, chunkIndex, batch[j], toVector(embeddings[j])]
        );
        total++;
      }
    }
    console.log(`  ${doc.url} → ${parts.length} chunks`);
  }
  console.log(`Done. Upserted ${total} chunks.`);
  process.exit(0);
}

main().catch((e) => { console.error(e); process.exit(1); });
