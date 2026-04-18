import os
from pathlib import Path

DOMAIN_MAP = {
    "01 - Payments Infrastructure": "payments",
    "02 - Banking & Regulation": "banking",
    "03 - Embedded Finance": "embedded-finance",
    "04 - Stablecoins & Crypto Rails": "stablecoins",
    "05 - Lending Infrastructure": "lending",
    "06 - Capital Markets": "capital-markets",
    "07 - Fraud & Risk": "fraud-risk",
    "08 - Frameworks & Models": "frameworks",
    "09 - Company Teardowns": "company-teardown",
    "10 - Regulatory Filings": "regulation"
}

def backfill():
    content_dir = Path("content")
    fixed_files = []

    for md_file in content_dir.rglob("*.md"):
        # Skip rules
        if md_file.name == "index.md" or "_Meta" in str(md_file) or "_Inbox" in str(md_file):
            continue
        
        rel_path = md_file.relative_to(content_dir)
        try:
            content = md_file.read_text(encoding="utf-8")
        except Exception as e:
            print(f"Error reading {md_file}: {e}")
            continue
        
        if not content.startswith("---"):
            print(f"Skipping {md_file}: No frontmatter block found.")
            # Maybe add a template if needed? The task says backfill incomplete, usually implies they have at least title.
            # I will wrap the content in frontmatter if it's missing entirely.
            content = "---\ntitle: " + md_file.stem + "\n---\n" + content
            
        parts = content.split("---", 2)
        if len(parts) < 3:
            # Handle cases with just title
            parts = ["", content.split("---")[1], "---".join(content.split("---")[2:])]
            
        frontmatter = parts[1]
        body = "---" + parts[2]
        lines = [line for line in frontmatter.strip().split("\n") if line.strip()]
        existing_keys = [line.split(":")[0].strip() for line in lines if ":" in line]
        
        new_fields = []
        
        # 1. domain
        if "domain" not in existing_keys:
            parent_folder = rel_path.parts[0]
            domain = DOMAIN_MAP.get(parent_folder, "general")
            new_fields.append(f"domain: {domain}")
            
        # 2. layer
        if "layer" not in existing_keys:
            # Simple inference logic
            plumbing = ["rails", "protocols", "networks", "infrastructure", "settlement", "clearing"]
            if any(word in content.lower() for word in plumbing):
                layer = "infrastructure"
            else:
                layer = "middleware"
            new_fields.append(f"layer: {layer}")
            
        # 3. last_reviewed
        if "last_reviewed" not in existing_keys:
            new_fields.append("last_reviewed: 2026-04-18")
            
        # 4. confidence
        if "confidence" not in existing_keys:
            # Detect MOCs: filename matches parent folder name or is very similar
            if md_file.stem in str(md_file.parent):
                conf = "stub"
            else:
                conf = "high"
            new_fields.append(f"confidence: {conf}")
            
        # 5. connections
        if "connections" not in existing_keys:
            new_fields.append("connections: []")
            
        if new_fields:
            # Reconstruct frontmatter
            updated_frontmatter = "\n".join(lines + new_fields)
            new_content = f"--- \n{updated_frontmatter}\n{body}"
            md_file.write_text(new_content, encoding="utf-8")
            fixed_files.append(str(md_file.relative_to(content_dir)))

    print(f"Fixed frontmatter on {len(fixed_files)} notes: {fixed_files}")

if __name__ == "__main__":
    backfill()
