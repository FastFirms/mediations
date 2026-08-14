#!/usr/bin/env node
/**
 * scripts/extract.mjs
 *
 * Reads sitemap.xml, finds each page's local index.html, strips HTML
 * boilerplate and outputs one JSON file per page into ./content/.
 * Run before ingest: `node scripts/extract.mjs`
 *
 * Output format (matches ingest.mjs loadDocuments()):
 *   { url, title, text }
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __dir = path.dirname(fileURLToPath(import.meta.url));
const REPO  = path.resolve(__dir, '..');
const SITEMAP = path.join(REPO, 'sitemap.xml');
const OUT_DIR = path.join(REPO, 'content');

const DOMAIN = 'https://www.mediationsaustralia.com.au';

// ---------------------------------------------------------------------------
// Parse sitemap — extract every <loc> URL
// ---------------------------------------------------------------------------
function parseSitemap() {
  const xml = fs.readFileSync(SITEMAP, 'utf8');
  const locs = [];
  for (const m of xml.matchAll(/<loc>(.*?)<\/loc>/g)) {
    locs.push(m[1].trim());
  }
  return locs;
}

// ---------------------------------------------------------------------------
// Map a sitemap URL to a local index.html path
// ---------------------------------------------------------------------------
function urlToLocalPath(url) {
  const slug = url.replace(DOMAIN, '').replace(/^\/|\/$/g, '');
  if (slug === '') return path.join(REPO, 'index.html');
  return path.join(REPO, slug, 'index.html');
}

// ---------------------------------------------------------------------------
// Extract <title> from HTML
// ---------------------------------------------------------------------------
function extractTitle(html) {
  const m = html.match(/<title>([\s\S]*?)<\/title>/i);
  if (!m) return '';
  return m[1]
    .replace(/\s*[|–—-]\s*Mediations Australia\s*$/i, '')
    .replace(/&amp;amp;/g, '&')  // double-encoded (e.g. HTML title tag)
    .replace(/&amp;/g, '&')
    .replace(/&#x27;/g, "'")
    .replace(/&[a-zA-Z0-9#]+;/g, ' ')
    .trim();
}

// ---------------------------------------------------------------------------
// Extract clean text from the <main> element only
// Strips: <nav> (crumb, ToC, site-nav), <header class="post-hero"> byline,
//         <aside> (bio block), <footer>, <script>, <style>, JSON-LD schema
// Keeps: H1, answer box, section headings, body paragraphs, tables, FAQ
// ---------------------------------------------------------------------------
function extractText(html) {
  // Isolate <main>
  const mainStart = html.indexOf('<main');
  const mainEnd   = html.lastIndexOf('</main>');
  if (mainStart === -1) {
    // fallback: use full body
    return cleanHtml(html);
  }
  let main = html.slice(mainStart, mainEnd + 7);

  // Drop script/style blocks
  main = main.replace(/<script[\s\S]*?<\/script>/gi, ' ');
  main = main.replace(/<style[\s\S]*?<\/style>/gi, ' ');

  // Drop JSON-LD schema blocks (large, useless for RAG)
  main = main.replace(/<script[^>]*type=["']application\/ld\+json["'][^>]*>[\s\S]*?<\/script>/gi, ' ');

  // Drop breadcrumb nav and post-TOC nav
  main = main.replace(/<nav[\s\S]*?<\/nav>/gi, ' ');

  // Drop post-hero header (author byline, category label — not content)
  main = main.replace(/<header[\s\S]*?<\/header>/gi, ' ');

  // Drop expert bio aside
  main = main.replace(/<aside[\s\S]*?<\/aside>/gi, ' ');

  // Drop CTA band section (booking prompt repeated on every page)
  main = main.replace(/<section[^>]*class="[^"]*cta[^"]*"[\s\S]*?<\/section>/gi, ' ');

  return cleanHtml(main);
}

function cleanHtml(html) {
  let t = html;
  // Decode common HTML entities
  t = t.replace(/&amp;/g, '&');
  t = t.replace(/&lt;/g, '<');
  t = t.replace(/&gt;/g, '>');
  t = t.replace(/&nbsp;/g, ' ');
  t = t.replace(/&#x27;/g, "'");
  t = t.replace(/&#x2019;/g, '’');
  t = t.replace(/&rarr;/g, '->');
  t = t.replace(/&mdash;/g, '—');
  t = t.replace(/&ndash;/g, '–');
  t = t.replace(/&[a-zA-Z0-9#]+;/g, ' ');
  // Strip remaining tags
  t = t.replace(/<[^>]+>/g, ' ');
  // Collapse whitespace
  t = t.replace(/[ \t]+/g, ' ');
  t = t.replace(/\n{3,}/g, '\n\n');
  return t.trim();
}

// ---------------------------------------------------------------------------
// Main
// ---------------------------------------------------------------------------
fs.mkdirSync(OUT_DIR, { recursive: true });

const urls = parseSitemap();
console.log(`Sitemap: ${urls.length} URLs`);

let written = 0;
let skipped = 0;

for (const url of urls) {
  const localPath = urlToLocalPath(url);
  if (!fs.existsSync(localPath)) {
    console.warn(`  SKIP (no file): ${url}`);
    skipped++;
    continue;
  }

  const html  = fs.readFileSync(localPath, 'utf8');
  const title = extractTitle(html);
  const text  = extractText(html);

  if (text.length < 100) {
    console.warn(`  SKIP (too short, ${text.length} chars): ${url}`);
    skipped++;
    continue;
  }

  const slug = url.replace(DOMAIN, '').replace(/^\/|\/$/g, '') || 'home';
  const outFile = path.join(OUT_DIR, slug.replace(/\//g, '--') + '.json');
  fs.writeFileSync(outFile, JSON.stringify({ url, title, text }, null, 0));
  written++;
}

console.log(`\nDone. Written: ${written}  Skipped: ${skipped}`);
console.log(`Content files in: ${OUT_DIR}`);
