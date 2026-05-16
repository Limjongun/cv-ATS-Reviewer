
import json
import random
import os

random.seed(42)

first_names = ["James","Michael","Robert","David","William","John","Thomas","Daniel","Matthew","Christopher",
               "Emily","Sarah","Jessica","Ashley","Amanda","Jennifer","Melissa","Nicole","Rachel","Lauren",
               "Kevin","Brian","Jason","Ryan","Eric","Mark","Steven","Andrew","Justin","Brandon",
               "Stephanie","Samantha","Megan","Katherine","Elizabeth","Christina","Amy","Rebecca","Lisa","Angela"]

last_names = ["Smith","Johnson","Williams","Brown","Jones","Garcia","Miller","Davis","Wilson","Martinez",
              "Anderson","Taylor","Thomas","Hernandez","Moore","Jackson","Martin","Lee","Thompson","White",
              "Harris","Clark","Lewis","Robinson","Walker","Young","Hall","Allen","King","Wright",
              "Scott","Torres","Nguyen","Hill","Flores","Green","Adams","Nelson","Baker","Carter"]

roles = [
    "Backend Engineer","Frontend Developer","Full Stack Developer","Data Analyst",
    "Machine Learning Engineer","DevOps Engineer","Software Engineer","Data Scientist",
    "Cloud Architect","Product Manager","QA Engineer","Mobile Developer","Site Reliability Engineer",
    "Cybersecurity Analyst","Database Administrator"
]

skills_pool = {
    "Backend Engineer": ["Python","Django","FastAPI","REST API","PostgreSQL","Redis","Docker","Linux","Celery","SQLAlchemy"],
    "Frontend Developer": ["JavaScript","TypeScript","React","Vue.js","HTML","CSS","Tailwind CSS","Next.js","Webpack","Jest"],
    "Full Stack Developer": ["Python","React","Node.js","MongoDB","PostgreSQL","Docker","REST API","GraphQL","Redis","CI/CD"],
    "Data Analyst": ["Python","SQL","Pandas","NumPy","Power BI","Tableau","Excel","Matplotlib","Seaborn","Jupyter"],
    "Machine Learning Engineer": ["Python","TensorFlow","PyTorch","Scikit-learn","Pandas","NumPy","HuggingFace","Docker","MLflow","FastAPI"],
    "DevOps Engineer": ["Docker","Kubernetes","Terraform","AWS","CI/CD","Jenkins","Linux","Ansible","Helm","Prometheus"],
    "Software Engineer": ["Java","Python","C++","Git","REST API","Docker","SQL","Agile","JUnit","Spring Boot"],
    "Data Scientist": ["Python","R","Scikit-learn","TensorFlow","SQL","Spark","Tableau","Jupyter","Pandas","Statistics"],
    "Cloud Architect": ["AWS","GCP","Azure","Terraform","Kubernetes","Docker","Linux","Networking","Security","IAM"],
    "Product Manager": ["Agile","JIRA","Roadmapping","SQL","Figma","Stakeholder Management","A/B Testing","OKR","Scrum","Analytics"],
    "QA Engineer": ["Selenium","Pytest","Postman","JIRA","CI/CD","Python","Manual Testing","JUnit","TestNG","Docker"],
    "Mobile Developer": ["Flutter","React Native","Kotlin","Swift","Android","iOS","Firebase","REST API","Git","Agile"],
    "Site Reliability Engineer": ["Kubernetes","Docker","Prometheus","Grafana","Linux","Python","Terraform","AWS","Incident Management","SLA"],
    "Cybersecurity Analyst": ["Network Security","Penetration Testing","SIEM","Python","Linux","Firewall","OWASP","Nmap","Wireshark","Incident Response"],
    "Database Administrator": ["PostgreSQL","MySQL","Oracle","SQL Server","MongoDB","Redis","Backup Recovery","Performance Tuning","Linux","Shell Scripting"]
}

universities = ["MIT","Stanford University","Harvard University","UC Berkeley","Carnegie Mellon University",
    "Georgia Tech","University of Michigan","University of Washington","UCLA","Columbia University",
    "Cornell University","NYU","Duke University","University of Texas at Austin","Purdue University"]

degrees = ["B.Sc Computer Science","B.Sc Information Technology","B.Eng Software Engineering",
           "B.Sc Data Science","M.Sc Computer Science","M.Sc Data Science","B.Sc Electrical Engineering"]

companies = ["Google","Amazon","Microsoft","Meta","Apple","Stripe","Airbnb","Uber","Netflix","Shopify",
    "Salesforce","Oracle","IBM","Accenture","Deloitte","Startup Hub","TechCorp","DataWorks",
    "CloudBase","InnovateTech","DevStream","AnalyticsLab","SecureNet","CodeFactory","BuildIt"]

cities = ["New York","San Francisco","Seattle","Austin","Boston","Chicago","Los Angeles","Denver","Atlanta","Portland"]

cert_pool = ["AWS Certified Solutions Architect","Google Cloud Professional","Docker Certified Associate",
             "Certified Kubernetes Administrator","TensorFlow Developer Certificate","PMP","Scrum Master","CISSP",
             "Oracle Certified Professional","Microsoft Azure Fundamentals"]

def make_raw_text(c):
    skills = ", ".join(c["skills"])
    company2 = c["companies"][1] if len(c["companies"]) > 1 else companies[random.randint(0,14)]
    raw = f"""{c['name']}
{c['role']}

Contact
-------
Email: {c['email']}
Phone: {c['phone']}
Location: {c['city']}
LinkedIn: linkedin.com/in/{c['name'].lower().replace(' ', '-')}

Summary
-------
Experienced {c['role']} with {c['experience_years']} years of hands-on experience in building scalable systems and delivering high-quality solutions. Passionate about clean code and continuous improvement.

Experience
----------
{c['role']}
{c['companies'][0]} | {2024 - random.randint(1, c['experience_years'])} - Present
- Developed and maintained core application features using {c['skills'][0]} and {c['skills'][1]}
- Collaborated with cross-functional teams to deliver projects on time
- Improved system performance by 30% through code optimization
- Mentored junior developers and conducted code reviews

Software Developer
{company2} | {2024 - c['experience_years'] - 2} - {2024 - random.randint(1, c['experience_years'])}
- Built RESTful APIs and maintained database schemas
- Participated in agile ceremonies including sprint planning and retrospectives
- Wrote unit and integration tests achieving 85% code coverage

Skills
------
{skills}

Education
---------
{c['degree']}
{c['university']} | {c['graduation_year']}
GPA: {round(random.uniform(3.2, 3.9), 2)}

Certifications
--------------
{c['certifications'][0] if c['certifications'] else 'N/A'}"""
    return raw.strip()

data = []
for i in range(1, 101):
    fname = random.choice(first_names)
    lname = random.choice(last_names)
    full_name = f"{fname} {lname}"
    role = random.choice(roles)
    skills = random.sample(skills_pool[role], k=random.randint(5, 8))
    exp = random.randint(1, 12)
    company_list = random.sample(companies, k=2)
    degree = random.choice(degrees)
    uni = random.choice(universities)
    grad_year = 2024 - exp - random.randint(0, 3)
    city = random.choice(cities)
    certs = random.sample(cert_pool, k=random.randint(0, 2))

    candidate = {
        "candidate_id": f"cv_{i:04d}",
        "file_name": f"resume_{i:04d}.pdf",
        "file_path": f"data/raw/cvs/resume_{i:04d}.pdf",
        "name": full_name,
        "email": f"{fname.lower()}.{lname.lower()}@email.com",
        "phone": f"+1-{random.randint(200,999)}-{random.randint(100,999)}-{random.randint(1000,9999)}",
        "city": city,
        "role": role,
        "skills": skills,
        "experience_years": exp,
        "companies": company_list,
        "degree": degree,
        "university": uni,
        "graduation_year": grad_year,
        "certifications": certs
    }

    raw_text = make_raw_text(candidate)

    record = {
        "candidate_id": f"cv_{i:04d}",
        "file_name": f"resume_{i:04d}.pdf",
        "file_path": f"data/raw/cvs/resume_{i:04d}.pdf",
        "source": "synthetic_pymupdf_simulation",
        "parser": "PyMuPDF 1.24.0",
        "pages": random.choice([1, 1, 1, 2, 2]),
        "text_raw": raw_text,
        "text_length": len(raw_text),
        "has_selectable_text": True,
        "needs_ocr": False,
        "extraction_status": "success",
        "extracted_at": f"2026-05-16T{random.randint(6,22):02d}:{random.randint(0,59):02d}:{random.randint(0,59):02d}+00:00"
    }
    data.append(record)

os.makedirs("output", exist_ok=True)
with open("output/raw_pymupdf_100.json", "w") as f:
    json.dump(data, f, indent=2)

with open("output/raw_pymupdf_100.jsonl", "w") as f:
    for r in data:
        f.write(json.dumps(r) + "\n")

print(f"Done: {len(data)} records")
print(f"JSON size: {os.path.getsize('output/raw_pymupdf_100.json')/1024:.1f} KB")
print(f"JSONL size: {os.path.getsize('output/raw_pymupdf_100.jsonl')/1024:.1f} KB")
