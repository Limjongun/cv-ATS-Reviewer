# TalentMatch-AI

TalentMatch-AI adalah sistem ekstraksi dan analisis CV berbasis NER (Named Entity Recognition) dan LLM reasoning. Sistem ini mampu:

- Mengekstrak entitas penting dari CV (nama, email, phone, jabatan, perusahaan, skill, pendidikan, bahasa, dsb.)
- Memfilter kandidat sesuai skill dan job requirement
- Memberikan rekomendasi dan reasoning kandidat menggunakan LLM.

---

## Workflow Produksi (Training NER)

1. Kumpulkan Dataset CV
   - Sumber: PDF, Word, atau CSV.
   - Bisa menggunakan dataset buatan atau real.
   - Simpan dalam format JSON awal.

2. Preprocessing & Annotation
   - Ambil raw_text dari setiap CV.
   - Tandai entitas penting: FULL_NAME, EMAIL, PHONE, JOB_TITLE, COMPANY, YEARS, DEGREE, MAJOR, UNIVERSITY, SKILL, LANGUAGE.

3. Generate TRAIN_DATA
   - Script Python membuat start-end positions untuk tiap entitas.
   - Menyimpan hasil ke train_data_ner.json.

4. Fine-tune spaCy NER
   - Load model dasar (en_core_web_sm).
   - Tambahkan semua label entitas.
   - Update model dengan TRAIN_DATA.
   - Simpan model ke folder cv_ner_model.

5. Validasi Model
   - Tes dengan CV baru.
   - Evaluasi akurasi entitas.

---

## Workflow Penggunaan (Inference & LLM Reasoning)

1. Input CV Baru
   - Format: PDF, DOCX, atau TXT.
   - Upload ke sistem atau batch processing.

2. Extract Teks
   - Gunakan PyMuPDF (fitz) atau library lainnya.
   - Simpan hasil raw_text.

3. NER Model Inference
   - Load model cv_ner_model.
   - Proses raw_text → ekstrak entitas.
   - Hasil: JSON terstruktur.

4. Filter Kandidat dengan Parameter
   - Parameter contoh: required_skills, job_title, language.
   - Gunakan Python untuk filter kandidat relevan.
   - Hitung matching score.

5. LLM Reasoning & Summary
   - Kandidat terfilter → kirim ke LLM.
   - Hasil LLM: summary kandidat, rekomendasi top kandidat, reasoning berdasarkan skill, pengalaman, dan bahasa.

6. Output
   - JSON siap pakai untuk HR system atau dashboard.

---

## Folder Struktur

TalentMatch-AI/
├── cv_dataset_field_specific.json    # Dataset CV awal
├── train_data_ner.json               # Dataset NER siap train
├── cv_ner_model/                     # Model NER hasil fine-tune
├── NER_train.py                       # Script train NER
├── NER_inference.py                   # Script inference + filter kandidat
├── LLM_reasoning.py                   # Script summary & reasoning top kandidat
├── README.md                          # Dokumentasi

---

## Teknologi & Library

- Python 3.11+
- spaCy → NER model
- PyMuPDF / fitz → PDF text extraction
- Optional LLM: OpenAI GPT, LLaMA, FLAN-T5, atau model lain
- JSON → structured output untuk sistem ATS / dashboard

---

## Catatan

- Workflow ini scalable: bisa batch processing PDF → JSON → filter → reasoning.
- LLM digunakan hanya untuk reasoning dan summary setelah kandidat difilter oleh Python.
- Dataset buatan atau real bisa digunakan untuk training NER, pastikan label lengkap dan tidak overlapping.
