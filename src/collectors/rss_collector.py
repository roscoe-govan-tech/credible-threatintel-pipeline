import feedparser
import hashlib


def create_hash(title, url):
    return hashlib.sha256(f"{title}{url}".encode()).hexdigest()


def fetch_rss(source):
    feed = feedparser.parse(source["url"])

    items = []

    for entry in feed.entries:
        title = entry.get("title", "")
        url = entry.get("link", "")
        summary = entry.get("summary", "")
        published = entry.get("published", "")

        if not title or not url:
            continue

        items.append({
            "source_name": source["name"],
            "source_tier": source["tier"],
            "category": source["category"],
            "title": title,
            "url": url,
            "summary": summary,
            "published_at": published,
            "content_hash": create_hash(title, url)
        })

    return items