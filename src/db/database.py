import sqlite3
from pathlib import Path


DB_PATH = Path("data/threatintel.db")
SCHEMA_PATH = Path("src/db/schema.sql")


# =========================
# CONNECTION
# =========================
def get_connection():
    DB_PATH.parent.mkdir(exist_ok=True)
    return sqlite3.connect(DB_PATH)


# =========================
# INIT DB
# =========================
def init_db():
    with get_connection() as conn:
        schema = SCHEMA_PATH.read_text(encoding="utf-8")
        conn.executescript(schema)
        conn.commit()


# =========================
# INSERT RAW ITEM (FIXED)
# =========================
def insert_raw_item(item):
    query = """
    INSERT OR IGNORE INTO raw_items (
        source_name,
        source_tier,
        category,
        title,
        url,
        summary,
        tldr,
        published_at,
        content_hash
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """

    with get_connection() as conn:
        cur = conn.execute(query, (
            item["source_name"],
            item["source_tier"],
            item["category"],
            item["title"],
            item["url"],
            item["summary"],
            item.get("tldr"),   # ✅ FIX: safely insert TL;DR
            item["published_at"],
            item["content_hash"]
        ))

        conn.commit()

        return cur.lastrowid