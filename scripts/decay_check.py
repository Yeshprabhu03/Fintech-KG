import yaml
import datetime
from pathlib import Path

STALE_DAYS = 180
CONTENT_DIR = Path("content")
DASHBOARD = Path("content/_Meta/Needs Review.md")
DASHBOARD.parent.mkdir(parents=True, exist_ok=True)

today = datetime.date.today()
stale = []
missing_date = []

for md_file in CONTENT_DIR.rglob("*.md"):
    if "_Inbox" in str(md_file) or "_Meta" in str(md_file) or md_file.name == "index.md":
        continue

    text = md_file.read_text(encoding="utf-8")
    if not text.startswith("---"):
        continue

    try:
        parts = text.split("---", 2)
        if len(parts) < 3:
            continue
        fm = yaml.safe_load(parts[1])
    except yaml.YAMLError:
        continue

    last = fm.get("last_reviewed")
    if not last:
        missing_date.append(md_file.stem)
        continue

    age = (today - last).days
    if age > STALE_DAYS:
        stale.append((md_file.stem, age, str(md_file.relative_to(CONTENT_DIR))))

stale.sort(key=lambda x: x[1], reverse=True)

lines = [
    "---",
    "title: Needs Review",
    "tags: [meta]",
    "---",
    f"\n# Needs Review",
    f"\n> Generated: {today}  |  Stale threshold: {STALE_DAYS} days\n",
    f"## Stale Notes ({len(stale)})\n",
]

for name, age, path in stale:
    lines.append(f"- [[{name}]] — {age} days since last review (`{path}`)")

if missing_date:
    lines.append(f"\n## Missing `last_reviewed` field ({len(missing_date)})\n")
    for name in missing_date:
        lines.append(f"- [[{name}]]")

DASHBOARD.write_text("\n".join(lines), encoding="utf-8")
print(f"Decay check done. {len(stale)} stale, {len(missing_date)} missing dates.")
