import google.generativeai as genai
import os
from datetime import date
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-1.5-flash")

def get_multiline_input(prompt):
    print(prompt)
    print("(Paste content, then type END on a new line and press Enter)")
    lines = []
    while True:
        line = input()
        if line.strip() == "END":
            break
        lines.append(line)
    return "\n".join(lines)

def main():
    print("=== Fintech Brain — Event Update ===\n")
    
    note_path_str = input("Path to existing note: ").strip()
    note_path = Path(note_path_str)
    
    if not note_path.exists():
        print(f"Error: {note_path} does not exist.")
        return
    
    existing_note = note_path.read_text(encoding="utf-8")
    new_info = get_multiline_input("\nPaste the new article or information:")
    
    diff_prompt = f"""You are updating a fintech knowledge vault note.

Existing note:
{existing_note}

New article/information:
{new_info}

What specifically needs updating in the existing note?
Return ONLY a bullet-point diff — new facts, changed numbers, outdated claims.
No prose, no explanation. Just the bullets."""

    print("\nAnalyzing changes...\n")
    diff_response = model.generate_content(diff_prompt)
    diff = diff_response.text
    
    print("=== Suggested Changes ===")
    print(diff)
    print("=========================\n")
    
    apply = input("Apply these changes automatically? (y/n): ").strip().lower()
    
    if apply == "y":
        update_prompt = f"""You are updating a fintech knowledge vault note.

Existing note:
{existing_note}

Apply these changes:
{diff}

Return the complete updated note with all frontmatter intact.
Update the last_reviewed field to {date.today().isoformat()}.
Return ONLY the markdown content, nothing else."""

        update_response = model.generate_content(update_prompt)
        note_path.write_text(update_response.text, encoding="utf-8")
        print(f"Updated: {note_path}")
    else:
        print("Changes not applied. Review manually.")

if __name__ == "__main__":
    main()
