import fitz  # PyMuPDF
import json
import re

def extract_text_from_pdf(pdf_path):
    """Extracts all text from a PDF file page by page."""
    doc = fitz.open(pdf_path)
    data = []
    for page_number, page in enumerate(doc, start=1):
        text = page.get_text("text")  # extract plain text
        data.append({
            "page_number": page_number,
            "text": text
        })
    return data

def parse_cv_text(text):
    """
    Parser to extract ATS-relevant fields from raw CV text.
    Supports: full_name, email, phone, job_title, company, years, skills, languages, summary
    """
    cv_data = {}

    # Extract email
    email_match = re.search(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)
    if email_match:
        cv_data["email"] = email_match.group(0)

    # Extract phone number (simple pattern)
    phone_match = re.search(r"(\+?\d[\d\s\-]{7,}\d)", text)
    if phone_match:
        cv_data["phone"] = phone_match.group(0)

    # Extract full name (first line assumed as name)
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    if lines:
        cv_data["full_name"] = lines[0]

    # Extract summary (look for SUMMARY section)
    summary_match = re.search(r"SUMMARY[:\n](.*?)(\n[A-Z]{2,}|$)", text, re.DOTALL | re.IGNORECASE)
    if summary_match:
        cv_data["summary"] = summary_match.group(1).strip()

    # Extract skills (Skills section)
    skills_match = re.search(r"(Skills|Technical Skills|Skillset)[:\n](.*?)(\n\n|\Z)", text, re.IGNORECASE | re.DOTALL)
    if skills_match:
        skills_text = skills_match.group(2)
        skills_list = [s.strip() for s in re.split(r"[,\n]", skills_text) if s.strip()]
        cv_data["skills"] = skills_list

    # Extract languages (LANGUAGES section)
    lang_match = re.search(r"LANGUAGES[:\n](.*?)(\n\n|\Z)", text, re.IGNORECASE | re.DOTALL)
    if lang_match:
        lang_text = lang_match.group(1)
        languages = [l.strip() for l in re.split(r"[,\n]", lang_text) if l.strip()]
        cv_data["languages"] = languages

    # Extract experience (simple heuristic)
    experience_pattern = re.compile(r"(?:EXPERIENCE|Experience)[:\n](.*?)(?:SKILLS|LANGUAGES|$)", re.IGNORECASE | re.DOTALL)
    exp_match = experience_pattern.search(text)
    experiences = []
    if exp_match:
        exp_text = exp_match.group(1)
        # Split by line with company/job info
        exp_entries = re.split(r"\n(?=[A-Z][a-z]+\s.*?(\d{4}|Present))", exp_text)
        for entry in exp_entries:
            lines_entry = entry.splitlines()
            if len(lines_entry) >= 2:
                # First line: Job Title
                title_line = lines_entry[0].strip()
                # Second line: Company + Years (try to extract)
                company_line = lines_entry[1].strip()
                years_match = re.search(r"(\d{4}-\d{4}|Present)", company_line)
                years = years_match.group(0) if years_match else ""
                # Company name: remove years
                company = company_line.replace(years, "").strip()
                description = " ".join([l.strip() for l in lines_entry[2:]]).strip()
                experiences.append({
                    "title": title_line,
                    "company": company,
                    "years": years,
                    "description": description
                })
    cv_data["experience"] = experiences

    # Optional: add full raw text
    cv_data["raw_text"] = text

    return cv_data

def pdf_to_json(pdf_path, json_path):
    """Convert a PDF CV to JSON file."""
    pages = extract_text_from_pdf(pdf_path)
    # Combine all pages for single CV parsing
    full_text = "\n".join([p["text"] for p in pages])
    cv_json = parse_cv_text(full_text)

    # Save to JSON
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(cv_json, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    pdf_file = "Andrew_Clark_CV.pdf"  # ganti path PDF
    json_file = "andrew_clark_cv.json"
    pdf_to_json(pdf_file, json_file)
    print(f"Converted {pdf_file} to {json_file}")