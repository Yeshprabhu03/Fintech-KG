import feedparser
import google.generativeai as genai
import os
import yaml
from datetime import date
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-1.5-flash")

SOURCES = [
    "https://www.bis.org/rss.htm",
    "https://feeds.feedburner.com/pymnts",
    "https://www.fintechbrainfood.com/feed",
    "https://www.thefintechtimes.com/feed/",
    "https://a16z.com/category/fintech/feed/",
    "https://www.americanbanker.com/feed",
    "https://www.bankingdive.com/feeds/news/",
]

INBOX_CAP = 20
INBOX = Path("content/_Inbox")
INBOX.mkdir(parents=True, exist_ok=True)

PROMPT_TEMPLATE = """You are building a fintech knowledge vault. Convert this article into a structured vault note.

Article title: {title}
Article content: {summary}

Return exactly this format — frontmatter then markdown body, nothing else:

---
title: {title}
tags: []
domain: (pick one: payments | banking | embedded-finance | stablecoins | capital-markets | fraud-risk | regulation | infrastructure)
layer: (pick one: infrastructure | middleware | application)
source: {url}
last_reviewed: {today}
confidence: stub
connections: []
---

## Summary
(2-3 sentences on the core mechanism or finding)

## Key Concepts
- (bullet points of important terms or ideas)

## Fintech Implications
(1-2 paragraphs on why this matters for fintech operators or builders)

## Open Questions
- (what is still unclear or worth researching further)
"""


def ingest():
    existing = list(INBOX.glob("*.md"))
    if len(existing) >= INBOX_CAP:
        print(f"Inbox at cap ({len(existing)} notes). Clear _Inbox before next run.")
        return

    added = 0
    for url in SOURCES:
        if len(existing) + added >= INBOX_CAP:
            break

        feed = feedparser.parse(url)
        for entry in feed.entries[:2]:
            title = entry.get("title", "Untitled")[:60]
            summary = entry.get("summary", entry.get("description", ""))[:3000]

            if not summary:
                continue

            safe_title = "".join(c for c in title if c.isalnum() or c in " -_")[:50]
            note_path = INBOX / f"{safe_title}.md"

            if note_path.exists():
                continue

            prompt = PROMPT_TEMPLATE.format(
                title=title,
                summary=summary,
                url=entry.get("link", url),
                today=date.today().isoformat(),
            )

            response = model.generate_content(prompt)
            note_path.write_text(response.text)
            print(f"Ingested: {safe_title}")
            added += 1

    print(f"Done. {added} new drafts in _Inbox.")


if __name__ == "__main__":
    ingest()
