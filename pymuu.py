import fitz  # PyMuPDF
import os
import json
import re

pdf_folder = "./generated_cvs"  # folder CV PDF
output_json = "cv_dataset.json"

dataset = []

def extract_text(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text("text") + "\n"
    return text

def parse_cv_text(text):
    cv = {}

    # Email
    email = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)
    cv["email"] = email[0] if email else ""

    # Phone
    phone = re.findall(r"\+?\d[\d\s\-]{7,}\d", text)
    cv["phone"] = phone[0] if phone else ""

    # Full name (anggap baris pertama)
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    cv["full_name"] = lines[0] if lines else ""

    # Field/job title (anggap baris kedua)
    cv["field"] = lines[1] if len(lines) > 1 else ""

    # Skills, Languages, Strengths parsing sederhana
    cv["skills"] = []
    cv["languages"] = []
    cv["strengths"] = []
    skills_match = re.search(r"SKILLS\n(.*?)\nLANGUAGES", text, re.DOTALL)
    if skills_match:
        cv["skills"] = [s.strip() for s in skills_match.group(1).split(",") if s.strip()]

    lang_match = re.search(r"LANGUAGES\n(.*?)\nSTRENGTHS", text, re.DOTALL)
    if lang_match:
        cv["languages"] = [s.strip() for s in lang_match.group(1).split(",") if s.strip()]

    strengths_match = re.search(r"STRENGTHS\n(.*)", text, re.DOTALL)
    if strengths_match:
        cv["strengths"] = [s.strip() for s in strengths_match.group(1).split("\n") if s.strip()]

    cv["raw_text"] = text
    return cv

# Proses semua PDF
for filename in os.listdir(pdf_folder):
    if filename.lower().endswith(".pdf"):
        path = os.path.join(pdf_folder, filename)
        text = extract_text(path)
        cv_data = parse_cv_text(text)
        dataset.append(cv_data)

# Simpan dataset JSON
with open(output_json, "w", encoding="utf-8") as f:
    json.dump(dataset, f, indent=2, ensure_ascii=False)

print(f"Dataset JSON siap: {output_json}, total CVs: {len(dataset)}")