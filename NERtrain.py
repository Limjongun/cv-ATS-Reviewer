import spacy
from spacy.training.example import Example
import json
import random

# Load base model
nlp = spacy.load("en_core_web_sm")  # pastikan sudah di-download
ner = nlp.get_pipe("ner")

# Tambahkan semua label
labels = [
    "FULL_NAME", "EMAIL", "PHONE", "JOB_TITLE", "COMPANY", "YEARS",
    "DEGREE", "MAJOR", "UNIVERSITY", "SKILL", "LANGUAGE"
]
for label in labels:
    ner.add_label(label)

# Load TRAIN_DATA
with open("train_data_ner.json", "r", encoding="utf-8") as f:
    TRAIN_DATA = json.load(f)

# Training
optimizer = nlp.create_optimizer()
n_iter = 20

for itn in range(n_iter):
    random.shuffle(TRAIN_DATA)
    losses = {}
    for text, annotations in TRAIN_DATA:
        doc = nlp.make_doc(text)
        example = Example.from_dict(doc, annotations)
        nlp.update([example], drop=0.3, losses=losses)
    print(f"Iteration {itn+1}, Losses: {losses}")

# Simpan model
nlp.to_disk("cv_ner_model")
print("Model NER saved to cv_ner_model")