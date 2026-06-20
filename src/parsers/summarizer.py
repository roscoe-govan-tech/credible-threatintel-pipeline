def generate_tldr(title, content):
    """
    Lightweight threat intelligence summarizer.
    Safe fallback version (no external API required).
    """

    if not content:
        return "No content available for summary."

    # Clean input (basic safety)
    content = content.strip()

    # =========================
    # RULE-BASED TL;DR ENGINE
    # =========================

    # Step 1: truncate noisy RSS text
    cleaned = content.replace("\n", " ").strip()

    # Step 2: limit size (RSS content can be messy/long)
    max_length = 400
    truncated = cleaned[:max_length]

    # Step 3: basic intelligence framing
    tldr = f"{title}. {truncated}"

    # Step 4: enforce SOC-style output length
    if len(tldr) > 500:
        tldr = tldr[:500] + "..."

    return tldr