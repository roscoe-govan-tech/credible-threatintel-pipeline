CREATE TABLE IF NOT EXISTS raw_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_name TEXT NOT NULL,
    source_tier INTEGER NOT NULL,
    category TEXT,
    title TEXT NOT NULL,
    url TEXT NOT NULL,
    summary TEXT,
    tldr TEXT,
    published_at TEXT,
    content_hash TEXT UNIQUE,
    collected_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);