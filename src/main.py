import yaml
from src.collectors.rss_collector import fetch_rss
from src.db.database import init_db, insert_raw_item
from src.parsers.summarizer import generate_tldr


# =========================
# LOAD SOURCES
# =========================
def load_sources():
    with open("config/sources.yml", "r", encoding="utf-8") as f:
        return yaml.safe_load(f)["rss_sources"]


# =========================
# PIPELINE RUNNER
# =========================
def run_pipeline():

    print("Initializing database...")
    init_db()

    sources = load_sources()
    print(f"Loaded {len(sources)} sources")

    total_inserted = 0

    # =========================
    # SOURCE LOOP
    # =========================
    for source in sources:
        print(f"\nCollecting from: {source['name']}")

        items = fetch_rss(source)

        # =========================
        # ITEM LOOP
        # =========================
        for item in items:

            # =========================
            # ENRICHMENT LAYER (TL;DR)
            # =========================
            try:
                title = item.get("title", "")
                summary = item.get("summary", "")

                content_for_summary = f"{title} {summary}".strip()

                # ALWAYS generate TL;DR (no conditional skipping)
                item["tldr"] = generate_tldr(title, content_for_summary)

            except Exception as e:
                print(f"TLDR generation failed: {e}")
                item["tldr"] = "No TLDR generated"

            # =========================
            # DEBUG CHECKPOINT (SAFE)
            # =========================
            print("FINAL ITEM BEFORE INSERT:")
            print(
                {
                    "title": item.get("title"),
                    "tldr": item.get("tldr"),
                    "source": item.get("source_name")
                }
            )

            # =========================
            # DATABASE INSERT
            # =========================
            row_id = insert_raw_item(item)

            if row_id:
                print(f"Inserted → {item['title'][:80]}")
                total_inserted += 1
            else:
                print(f"Skipped duplicate → {item['title'][:80]}")

    print(f"\nDONE. Total inserted: {total_inserted}")


# =========================
# ENTRY POINT
# =========================
if __name__ == "__main__":
    run_pipeline()