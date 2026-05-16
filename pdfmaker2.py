from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib import colors
import random
import os

# Output folder
output_dir = "generated_cvs"
os.makedirs(output_dir, exist_ok=True)

# ----------------- Data Pools -----------------
first_names = [
    "Andrew", "Thomas", "Rina", "Kevin", "Lina", "Aditya", "Sari", "Bima",
    "Miguel", "Juan", "Carlos", "Sophia", "Isabella", "Emma", "Oliver",
    "Liam", "Noah", "Ethan", "Fatima", "Aisha", "Dewi", "Agus", "Budi",
    "Rahayu", "Surya", "Putri", "Hendra", "Joko", "Tari", "Maria", "Ana",
    "Santiago", "Diego", "Julian", "Elena", "Victoria", "Hannah", "Mia",
    "Leo", "Sebastian", "Aria", "Kirana", "Nadia", "Rafael", "Felipe",
    "Miguelina", "Esteban", "Andi", "Wulan", "Galih", "Bayu", "Dian"
]

last_names = [
    "Clark", "Hermanicus", "Setiawan", "Wijaya", "Pratama", "Rahman", "Gunawan", "Santoso",
    "Putri", "Saputra", "Lestari", "Suryanto", "Wibowo", "Cahyo", "Anggraeni", "Rizky",
    "Sukma", "Wardhana", "Purnomo", "Hidayat", "Santika", "Wijayanto", "Prabowo",
    "Garcia", "Martinez", "Rodriguez", "Lopez", "Hernandez", "Sanchez", "Perez",
    "Gomez", "Diaz", "Torres", "Ramirez", "Flores", "Vargas", "Castillo", "Morales",
    "Kim", "Lee", "Nguyen", "Patel", "Singh", "Ali", "Khan", "Chen", "Wong", "Tan"
]

skills_pool = {
    # IT / Engineering
    "AI Engineer": ["Python", "TensorFlow", "PyTorch", "Machine Learning", "Deep Learning", "Data Analysis"],
    "Data Scientist": ["Python", "R", "SQL", "Statistics", "Machine Learning", "Data Visualization"],
    "Software Engineer": ["Java", "C++", "Python", "Git", "Algorithms", "Data Structures"],
    "DevOps Engineer": ["AWS", "Docker", "Kubernetes", "CI/CD", "Monitoring", "Terraform"],
    "Cloud Architect": ["AWS", "Azure", "GCP", "Cloud Design", "Networking"],
    "Cybersecurity Analyst": ["Network Security", "Penetration Testing", "Firewall Management", "SIEM"],
    "Frontend Developer": ["HTML", "CSS", "JavaScript", "React", "Vue.js"],
    "Backend Developer": ["Node.js", "Python", "Django", "Database Design", "API Development"],
    "Full Stack Developer": ["Frontend", "Backend", "Database", "API", "DevOps"],
    "Machine Learning Engineer": ["Python", "TensorFlow", "PyTorch", "Data Preprocessing", "Model Deployment"],

    # Management / Leadership
    "Project Manager": ["Project Management", "Leadership", "Cost Management", "Excel", "PowerPoint", "Mentorship"],
    "Product Manager": ["Roadmapping", "User Research", "Backlog Management", "Analytics", "Leadership"],
    "Program Manager": ["Strategic Planning", "Stakeholder Management", "Budgeting", "Risk Management"],
    "Operations Manager": ["Process Improvement", "Logistics", "Supply Chain", "Leadership", "KPI Tracking"],
    "Business Analyst": ["Requirement Gathering", "Data Analysis", "Process Mapping", "Documentation"],

    # Design / Creative
    "UX Designer": ["Prototyping", "Adobe XD", "User Research", "Figma", "Creativity"],
    "UI Designer": ["Sketch", "Figma", "Adobe XD", "CSS", "HTML"],
    "Graphic Designer": ["Photoshop", "Illustrator", "Branding", "Typography", "Creativity"],
    "Creative Director": ["Team Leadership", "Brand Strategy", "Art Direction", "Creative Thinking"],
    "Visual Designer": ["Design Systems", "UI Kits", "Illustration", "Layout", "Typography"],

    # Marketing / Sales
    "Marketing Manager": ["SEO", "Content Strategy", "Social Media", "Branding", "Analytics"],
    "Digital Marketing Specialist": ["PPC", "SEO", "Email Marketing", "Social Media Ads", "Google Analytics"],
    "Social Media Manager": ["Community Management", "Content Creation", "Analytics", "Social Media Strategy"],
    "Content Strategist": ["Content Planning", "SEO", "Blog Writing", "Analytics", "Brand Voice"],
    "SEO Specialist": ["Keyword Research", "On-page SEO", "Backlinking", "Analytics", "SEO Tools"],
    "Sales Executive": ["Lead Generation", "CRM", "Negotiation", "Presentation Skills", "Closing Deals"],
    "Account Manager": ["Client Management", "Upselling", "CRM", "Reporting", "Communication"],
    "Brand Manager": ["Brand Strategy", "Marketing Plan", "Campaign Management", "Analysis"],

    # HR / People
    "HR Manager": ["Recruitment", "Talent Management", "Payroll", "Training", "Compliance"],
    "Recruitment Specialist": ["Sourcing", "Interviewing", "ATS", "Onboarding", "Candidate Experience"],
    "Talent Acquisition Manager": ["Employer Branding", "Sourcing", "Interviewing", "HR Metrics"],
    "HR Generalist": ["Employee Relations", "HR Policies", "Payroll", "Compliance", "Documentation"],
    "Training & Development Specialist": ["Learning & Development", "Instructional Design", "Workshops", "Assessment"],

    # Finance / Accounting
    "Financial Analyst": ["Excel", "Financial Modelling", "Budgeting", "Forecasting", "Data Analysis"],
    "Accountant": ["Accounting", "Tax", "Audit", "QuickBooks", "Financial Reporting"],
    "Controller": ["Budgeting", "Financial Reporting", "Internal Controls", "Cash Flow Management"],
    "Investment Analyst": ["Valuation", "Financial Modelling", "Market Research", "Portfolio Analysis"],
    "Payroll Specialist": ["Payroll Processing", "Compliance", "Taxes", "HRIS"],

    # R&D / Science
    "Research Scientist": ["Experimental Design", "Data Analysis", "Lab Techniques", "Documentation"],
    "Lab Technician": ["Sample Preparation", "Testing Procedures", "Equipment Handling", "Documentation"],
    "Pharmaceutical Scientist": ["Drug Formulation", "Testing", "Compliance", "Lab Reporting"],
    "Data Researcher": ["Data Collection", "Data Cleaning", "Analysis", "Reporting"],

    # Customer Service / Support
    "Customer Support Specialist": ["Customer Service", "CRM Tools", "Problem Solving", "Communication"],
    "Client Success Manager": ["Client Onboarding", "Relationship Management", "Reporting", "Retention"],
    "Call Center Supervisor": ["Team Management", "Scheduling", "KPI Tracking", "Conflict Resolution"],

    # Operations / Logistics
    "Operations Coordinator": ["Scheduling", "Logistics", "Inventory", "Process Improvement"],
    "Supply Chain Manager": ["Procurement", "Logistics", "Vendor Management", "Inventory", "Forecasting"],
    "Logistics Analyst": ["Route Optimization", "Data Analysis", "Reporting", "Inventory Control"],

    # Executive
    "CEO": ["Leadership", "Strategy", "Decision Making", "Team Building"],
    "COO": ["Operations Management", "Leadership", "Process Improvement", "Strategy"],
    "CTO": ["Technology Strategy", "Team Leadership", "Architecture Design", "Innovation"],
    "CFO": ["Financial Planning", "Budgeting", "Risk Management", "Investor Relations"],
    "Executive Assistant": ["Scheduling", "Communication", "Organization", "Documentation"]
}
languages_pool = ["English (Fluent)", "Indonesian (Native)", "Spanish (Advanced)", "French (Basic)"]

strengths_pool = [
    "Creative Problem Solving: Utilize creative solutions to tackle challenges.",
    "Strong Leadership: Experienced in leading and mentoring teams.",
    "Efficient Resource Allocation: Spearheaded reorganization of projects reducing costs.",
    "Highly adaptable and quick learner, able to thrive in fast-paced environments.",
    "Excellent communication skills, able to convey complex ideas clearly and effectively.",
    "Proven track record of delivering results under pressure and meeting tight deadlines.",
    "Strong analytical skills, able to break down complex problems and identify effective solutions.",
    "Collaborative team player, experienced in working with cross-functional teams to achieve common goals.",
    "Passionate about continuous learning and professional development, always seeking opportunities to grow skills and knowledge."
]

fields = [
    "AI Engineer", "Data Scientist", "Software Engineer", "DevOps Engineer", "Cloud Architect",
    "Cybersecurity Analyst", "Project Manager", "Product Manager", "Program Manager",
    "UX Designer", "UI Designer", "Graphic Designer", "Marketing Manager", "Digital Marketing Specialist",
    "HR Manager", "Recruitment Specialist", "Financial Analyst", "Accountant", "Customer Support Specialist"
]

universities = [
    "Stamford University", "Universitas Indonesia", "MIT", "Institut Teknologi Bandung",
    "Harvard University", "Stanford University", "University of California, Berkeley",
    "University of Oxford"
]

companies = [
    "IBM", "Microsoft", "Apple Inc.", "Google", "TechCorp", "NextGen Labs",
    "NeuralTech Labs","DataWorks Inc.","CloudSolutions", "CyberSecure Inc.","Innovatech"
]



# ----------------- Generate 100 CVs -----------------
N = 500

fields = list(skills_pool.keys())

for i in range(N):
    first = random.choice(first_names)
    last = random.choice(last_names)
    full_name = f"{first} {last}"
    field = random.choice(fields)
    university = random.choice(universities)
    email = f"{first.lower()}.{last.lower()}@gmail.com"
    phone = f"+62-{random.randint(800,899)}-{random.randint(1000,9999)}-{random.randint(1000,9999)}"

    # Experience
    num_exp = random.randint(1,3)
    experiences = []
    skills_for_field = skills_pool.get(field, ['General'])
    for _ in range(num_exp):
        title = f"{field} {random.choice(['Intern','Junior','Senior'])}"
        company = random.choice(companies)
        start_year = random.randint(2015,2021)
        end_year = f"{start_year + random.randint(1,3)}" if random.random() > 0.2 else "Present"
        sample_skills_for_desc = random.sample(skills_for_field, k=min(3, len(skills_for_field)))
        desc = f"Worked at {company} focusing on {', '.join(sample_skills_for_desc)}."
        experiences.append([title, company, f"{start_year}-{end_year}", desc])

    # Skills, Languages, Strengths
    skills = random.sample(skills_for_field, k=min(5, len(skills_for_field)))
    languages = random.sample(languages_pool, k=2)
    strengths = random.sample(strengths_pool, k=3)

    # Generate PDF
    pdf_file = os.path.join(output_dir, f"{first}_{last}_CV.pdf")
    doc = SimpleDocTemplate(pdf_file, pagesize=A4, rightMargin=40, leftMargin=40, topMargin=40, bottomMargin=40)
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle('Title', parent=styles['Heading1'], fontSize=20, leading=22, spaceAfter=6)
    heading_style = ParagraphStyle('Heading2', parent=styles['Heading2'], fontSize=14, spaceBefore=12, spaceAfter=6)
    normal_style = styles['Normal']

    story = []

    # Header
    story.append(Paragraph(full_name, title_style))
    story.append(Paragraph(field, ParagraphStyle('Header2', fontSize=12, textColor=colors.HexColor('#0077CC'), spaceAfter=12)))
    story.append(Paragraph(f"📞 {phone} | ✉ {email} | 🌐 linkedin.com | 📍 City, Country", normal_style))
    story.append(Spacer(1, 12))

    # Summary
    summary = f"{full_name} is a professional {field} graduated from {university} with experience in {', '.join(skills)}."
    story.append(Paragraph("SUMMARY", heading_style))
    story.append(Paragraph(summary, normal_style))
    story.append(Spacer(1,12))

    # Experience
    story.append(Paragraph("EXPERIENCE", heading_style))
    for title, company, years, desc in experiences:
        story.append(Paragraph(f"<b>{title}</b> | <font color='blue'>{company}</font> | {years}", normal_style))
        story.append(Paragraph(desc, normal_style))
        story.append(Spacer(1,6))

    # Skills
    story.append(Paragraph("SKILLS", heading_style))
    story.append(Paragraph(", ".join(skills), normal_style))
    story.append(Spacer(1,12))

    # Languages
    story.append(Paragraph("LANGUAGES", heading_style))
    story.append(Paragraph(", ".join(languages), normal_style))
    story.append(Spacer(1,12))

    # Strengths
    story.append(Paragraph("STRENGTHS", heading_style))
    for s in strengths:
        story.append(Paragraph(s, normal_style))
        story.append(Spacer(1,6))

    # Build PDF
    doc.build(story)
    print(f"Generated CV: {pdf_file}")