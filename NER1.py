import json

# Buka dataset CV
with open("cv_dataset_field_specific.json", "r", encoding="utf-8") as f:
    data = json.load(f)

TRAIN_DATA = []

for cv in data:
    text = cv["raw_text"]
    entities = []

    # full_name
    start = text.find(cv["full_name"])
    if start != -1:
        entities.append((start, start+len(cv["full_name"]), "FULL_NAME"))

    # email
    start = text.find(cv["email"])
    if start != -1:
        entities.append((start, start+len(cv["email"]), "EMAIL"))

    # phone
    start = text.find(cv["phone"])
    if start != -1:
        entities.append((start, start+len(cv["phone"]), "PHONE"))

    # skills
    for skill in cv["skills"]:
        start = text.find(skill)
        if start != -1:
            entities.append((start, start+len(skill), "SKILL"))

    TRAIN_DATA.append((text, {"entities": entities}))

print(f"Prepared {len(TRAIN_DATA)} samples for NER training")

# Simpan hasil TRAIN_DATA ke file JSON
output_file = "train_data_ner.json"

# Perbaikan: unpack tuple biasa
train_data_serializable = [
    [text, item_dict] for text, item_dict in TRAIN_DATA
]

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(train_data_serializable, f, indent=2, ensure_ascii=False)

print(f"Saved TRAIN_DATA to {output_file}")