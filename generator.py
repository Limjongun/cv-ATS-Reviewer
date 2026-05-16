import json
import random

# Contoh data untuk variasi
first_names = ["Thomas", "Alya", "Bima", "Rina", "Kevin", "Sari", "Aditya", "Lina","Dewi", "Fajar","Rizky", "Maya", "Arif", "Nina", "Dian", "Eka", "Fauzi", "Gina", "Hendra", "Indra"]
last_names = ["Hermanicus", "Santoso", "Putri", "Wijaya", "Pratama", "Rahman", "Gunawan", "Setiawan"]
fields = ["AI Engineer", "Data Scientist", "Software Engineer", "Web Developer", "Cloud Architect", "Cybersecurity Analyst",
          "Project Manager", "UX Designer", "Digital Marketer", "Financial Analyst", "HR Specialist"]
universities = ["Stamford University", "Universitas Indonesia", "Institut Teknologi Bandung", "Harvard University", "MIT"]

# Pool skill diperluas, IT + non-IT
skills_pool = [
    "Python", "Java", "SQL", "TensorFlow", "PyTorch", "Machine Learning", "Deep Learning", "Data Analysis", "AWS", "Docker", # IT
    "Project Management", "Leadership", "Communication", "Teamwork", "Problem Solving", "Public Speaking", # Manajemen
    "Graphic Design", "Adobe Photoshop", "UI/UX Design", "Creativity", # Desain
    "Financial Analysis", "Accounting", "Budgeting", # Bisnis
    "Marketing", "SEO", "Content Creation", # Marketing
    "Negotiation", "Research", "Languages" # Lain-lain
]

languages_pool = ["English (Fluent)", "Indonesian (Native)", "Spanish (Intermediate)", "French (Basic)"]

def generate_cv(id):
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    full_name = f"{first_name} {last_name}"
    email = f"{first_name.lower()}.{last_name.lower()}@example.com"
    phone = f"+62-{random.randint(800,899)}-{random.randint(1000,9999)}-{random.randint(1000,9999)}"
    field = random.choice(fields)
    university = random.choice(universities)

    # Random skills and languages
    skills = random.sample(skills_pool, k=random.randint(4,8))
    languages = random.sample(languages_pool, k=random.randint(1,2))

    # Simulate raw_text
    raw_text = f"{full_name}\n{field}\nEmail: {email} | Phone: {phone}\nEducation\nDegree\nMajor\nUniversity\nYear\nBachelor of Science\n{field}\n{university}\n2022\nExperience\nTitle\nCompany\nYears\nDescription\n{field} Intern\nTechCorp\n2022-2023\nWorked on projects using {', '.join(skills)}.\nJunior {field}\nNextGen Labs\n2023-Present\nImplemented solutions using {', '.join(skills)}.\nSkills\n{', '.join(skills)}\nLanguages\n{', '.join(languages)}\n"

    return {
        "id": id,
        "full_name": full_name,
        "email": email,
        "phone": phone,
        "field": field,
        "skills": skills + languages,  # sesuai format NER
        "raw_text": raw_text
    }

# Generate N dataset
N = 300  # bisa diganti 1000 atau lebih
dataset = [generate_cv(i+1) for i in range(N)]

# Simpan ke JSON
with open("cv_dataset_extended.json", "w", encoding="utf-8") as f:
    json.dump(dataset, f, indent=2, ensure_ascii=False)

print(f"Generated {N} CV datasets with extended skills to cv_dataset_extended.json")