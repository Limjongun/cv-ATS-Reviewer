import json
import random

# Variasi nama dan universitas
first_names = ["Thomas", "Alya", "Bima", "Rina", "Kevin", "Sari", "Aditya", "Lina"]
last_names = ["Hermanicus", "Santoso", "Putri", "Wijaya", "Pratama", "Rahman", "Gunawan", "Setiawan"]
universities = ["Stamford University", "Universitas Indonesia", "Institut Teknologi Bandung", "Harvard University", "MIT"]

# Bidang dan skill relevan per bidang
fields_skills = {
    "AI Engineer": ["Python", "TensorFlow", "PyTorch", "Machine Learning", "Deep Learning", "Data Analysis", "AWS", "Docker"],
    "Data Scientist": ["Python", "R", "SQL", "Statistics", "Data Visualization", "Machine Learning", "Deep Learning"],
    "Software Engineer": ["Python", "Java", "C++", "Git", "Agile", "SQL", "Docker", "Testing"],
    "Web Developer": ["HTML", "CSS", "JavaScript", "React", "Node.js", "SQL", "Git"],
    "Cloud Architect": ["AWS", "Azure", "Cloud Security", "Networking", "Terraform", "Docker"],
    "Cybersecurity Analyst": ["Network Security", "Penetration Testing", "Firewalls", "Python", "Risk Assessment"],
    "Project Manager": ["Project Management", "Agile", "Scrum", "Leadership", "Communication", "Risk Management"],
    "UX Designer": ["UI/UX Design", "Adobe XD", "Figma", "User Research", "Prototyping", "Creativity"],
    "Digital Marketer": ["SEO", "Content Creation", "Social Media Marketing", "Google Analytics", "Email Marketing"],
    "Financial Analyst": ["Financial Analysis", "Accounting", "Excel", "Budgeting", "Forecasting"],
    "HR Specialist": ["Recruitment", "Employee Relations", "HR Policies", "Performance Management", "Payroll"]
}

languages_pool = ["English (Fluent)", "Indonesian (Native)", "Spanish (Intermediate)", "French (Basic)"]

def generate_cv(id):
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    full_name = f"{first_name} {last_name}"
    email = f"{first_name.lower()}.{last_name.lower()}@example.com"
    phone = f"+62-{random.randint(800,899)}-{random.randint(1000,9999)}-{random.randint(1000,9999)}"
    field = random.choice(list(fields_skills.keys()))
    university = random.choice(universities)

    # Pilih skill sesuai bidang
    skills = random.sample(fields_skills[field], k=random.randint(3,5))
    languages = random.sample(languages_pool, k=random.randint(1,2))

    # Raw text simulation
    raw_text = f"{full_name}\n{field}\nEmail: {email} | Phone: {phone}\nEducation\nDegree\nMajor\nUniversity\nYear\nBachelor of Science\n{field}\n{university}\n2022\nExperience\nTitle\nCompany\nYears\nDescription\n{field} Intern\nTechCorp\n2022-2023\nWorked on projects using {', '.join(skills)}.\nJunior {field}\nNextGen Labs\n2023-Present\nImplemented solutions using {', '.join(skills)}.\nSkills\n{', '.join(skills)}\nLanguages\n{', '.join(languages)}\n"

    return {
        "id": id,
        "full_name": full_name,
        "email": email,
        "phone": phone,
        "field": field,
        "skills": skills + languages,
        "raw_text": raw_text
    }

# Generate dataset
N = 500  # Bisa ganti 1000+
dataset = [generate_cv(i+1) for i in range(N)]

# Simpan ke JSON
with open("cv_dataset_field_specific.json", "w", encoding="utf-8") as f:
    json.dump(dataset, f, indent=2, ensure_ascii=False)

print(f"Generated {N} field-specific CV datasets to cv_dataset_field_specific.json")