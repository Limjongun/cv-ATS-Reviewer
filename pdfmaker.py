from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Frame, Image
from reportlab.lib import colors
from reportlab.lib.units import cm

# Nama file PDF output
pdf_file = "Andrew_Clark_CV.pdf"

# Membuat dokumen
doc = SimpleDocTemplate(pdf_file, pagesize=A4, rightMargin=40, leftMargin=40, topMargin=40, bottomMargin=40)

# Styles
styles = getSampleStyleSheet()
title_style = ParagraphStyle('Title', parent=styles['Heading1'], fontSize=20, leading=22, spaceAfter=6)
heading_style = ParagraphStyle('Heading2', parent=styles['Heading2'], fontSize=14, spaceBefore=12, spaceAfter=6)
normal_style = styles['Normal']
italic_style = ParagraphStyle('Italic', parent=styles['Normal'], fontSize=10, italic=True)

# Konten CV
story = []

# Header
story.append(Paragraph("ANDREW CLARK", title_style))
story.append(Paragraph("Experienced Project Manager | IT | Leadership | Cost Management", ParagraphStyle('Header2', fontSize=12, textColor=colors.HexColor('#0077CC'), spaceAfter=12)))

# Contact info
contact_info = "📞 +1-541-754-3010  |  ✉ help@enhancv.com  |  🌐 linkedin.com  |  📍 New York, NY, USA"
story.append(Paragraph(contact_info, normal_style))
story.append(Spacer(1, 12))

# Two-column frame
from reportlab.platypus import KeepTogether

# Summary - kiri atas
summary = "With over 12 years of experience in project management, William Davis brings a wealth of expertise in managing complex IT projects, particularly in cloud technology. He has a proven ability to enhance efficiency, having managed a $2M project portfolio, resulting in significant cost reductions."
story.append(Paragraph("SUMMARY", heading_style))
story.append(Paragraph(summary, normal_style))
story.append(Spacer(1,12))

# Experience
story.append(Paragraph("EXPERIENCE", heading_style))
experience_data = [
    ["Senior IT Project Manager", "IBM", "2018-2023", "Managed complex IT projects with focus on timing, functionality, and cost efficiency. Oversaw $2M project portfolio resulting in 15% cost reduction."] ,
    ["IT Project Manager", "Microsoft", "2014-2018", "Directed project planning and execution ensuring project goals and requirements were met."]
]
for title, company, years, desc in experience_data:
    story.append(Paragraph(f"<b>{title}</b> | <font color='blue'>{company}</font> | {years}", normal_style))
    story.append(Paragraph(desc, normal_style))
    story.append(Spacer(1,6))

# Skills - kanan
story.append(Paragraph("SKILLS", heading_style))
skills = [
    "Project Management", "Leadership", "Cost Management", "Cloud Knowledge",
    "Project Management Software Tools", "Problem Solving", "Excel", "Access", "Word", "PowerPoint", "PowerBI",
    "Mentorship", "Organizational Skills"
]
skills_text = ', '.join(skills)
story.append(Paragraph(skills_text, normal_style))
story.append(Spacer(1,12))

# Languages
story.append(Paragraph("LANGUAGES", heading_style))
languages = ["English (Native)", "Spanish (Advanced)", "Arabic (Beginner)"]
story.append(Paragraph(', '.join(languages), normal_style))
story.append(Spacer(1,12))

# Strengths
story.append(Paragraph("STRENGTHS", heading_style))
strengths = [
    "Creative Problem Solving: Utilize creative solutions to tackle challenges.",
    "Strong Leadership: Experienced in leading and mentoring teams.",
    "Efficient Resource Allocation: Spearheaded reorganization of projects reducing costs."
]
for s in strengths:
    story.append(Paragraph(s, normal_style))
    story.append(Spacer(1,6))

# Build PDF
doc.build(story)
print(f"PDF CV generated: {pdf_file}")