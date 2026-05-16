# headless_ner.py
import os
import fitz  # PyMuPDF
import spacy
import json

# Load NER model
nlp = spacy.load("cv_ner_model")

# ---------------- Helper Functions ----------------
def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text("text") + "\n"
    return text

def ner_inference(text):
    doc = nlp(text)
    result = {"FULL_NAME": [], "EMAIL": [], "PHONE": [], "JOB_TITLE": [],
              "COMPANY": [], "YEARS": [], "DEGREE": [], "MAJOR": [],
              "UNIVERSITY": [], "SKILL": [], "LANGUAGE": []}
    for ent in doc.ents:
        result.setdefault(ent.label_, []).append(ent.text)
    return result

def calculate_score(ner_data, job_type, required_skills):
    score = 0
    if any(job_type.lower() in jt.lower() for jt in ner_data.get("JOB_TITLE", [])):
        score += 2
    skill_matches = set(ner_data.get("SKILL", [])) & set(required_skills)
    score += len(skill_matches)
    return score, skill_matches

# ---------------- Main Script ----------------
# Parameter
pdf_folder = "generated_cvs"  # folder yang berisi semua PDF
job_type = "Project Manager"
required_skills = ["Project Management","PowerBI"]

results = []

for file_name in os.listdir(pdf_folder):
    if file_name.lower().endswith(".pdf"):
        pdf_path = os.path.join(pdf_folder, file_name)
        text = extract_text_from_pdf(pdf_path)
        ner_data = ner_inference(text)
        score, matched_skills = calculate_score(ner_data, job_type, required_skills)
        results.append({
            "pdf_file": file_name,
            "score": score,
            "matched_skills": list(matched_skills),
            "ner_data": ner_data
        })

# Urutkan berdasarkan score descending
results.sort(key=lambda x: x["score"], reverse=True)

# Tampilkan top 5
print("=== Top 5 Kandidat ===")
for r in results[:5]:
    print(f"PDF: {r['pdf_file']} | Score: {r['score']} | Skills matched: {', '.join(r['matched_skills'])}")
    print(f"Name: {', '.join(r['ner_data'].get('FULL_NAME', []))}")
    print(f"Email: {', '.join(r['ner_data'].get('EMAIL', []))}")
    print("-"*60)

# Simpan semua hasil ke JSON
with open("ner_results1.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

print("All results saved to ner_results.json")