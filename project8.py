import re
from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Resume', 0, 1, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(2)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

def sanitize_text(text):
    replacements = {
        '\u2018': "'",  
        '\u2019': "'",  
        '\u201C': '"',  
        '\u201D': '"',  
        '\u2014': '-',  
        '\u2013': '-',  
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text

def create_resume(name, contact, summary, experience, education, skills):
    pdf = PDF()
    pdf.add_page()

    name = sanitize_text(name)
    contact = sanitize_text(contact)
    summary = sanitize_text(summary)
    experience = sanitize_text(experience)
    education = sanitize_text(education)
    skills = sanitize_text(skills)

    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 10, name, 0, 1, 'C')
    pdf.set_font('Arial', '', 12)
    pdf.cell(0, 10, contact, 0, 1, 'C')
    pdf.ln(10)

    pdf.chapter_title('Summary')
    pdf.chapter_body(summary)

    pdf.chapter_title('Experience')
    pdf.chapter_body(experience)

    pdf.chapter_title('Education')
    pdf.chapter_body(education)

    pdf.chapter_title('Skills')
    pdf.chapter_body(skills)

    pdf.output('resume.pdf')

def check_ats_friendly(resume_text):
    issues = []

    if not re.search(r'\b(Experience|Education|Skills|Summary)\b', resume_text, re.IGNORECASE):
        issues.append("Missing key sections: Experience, Education, Skills, or Summary.")

    if len(resume_text.split()) < 300:
        issues.append("Resume is too short. Aim for at least 300 words.")

    keywords = ["teamwork", "leadership", "communication", "project management", "analysis"]
    keyword_found = any(keyword in resume_text.lower() for keyword in keywords)
    if not keyword_found:
        issues.append("Consider including keywords relevant to your industry.")

    special_chars = re.findall(r'[^\w\s,.]', resume_text)
    if special_chars:
        issues.append(f"Special characters found: {set(special_chars)}")

    if re.search(r'\bHeader\b', resume_text, re.IGNORECASE):
        issues.append("Avoid using headers or footers, as they can be ignored by ATS.")

    if re.search(r'\b(image|graphic|picture)\b', resume_text, re.IGNORECASE):
        issues.append("Avoid using images or graphics, as they may not be parsed correctly.")

    return issues if issues else ["Your resume appears to be ATS-friendly!"]

def main():
    print("Welcome to the Resume Builder!")
    
    name = input("Enter your name: ")
    contact = input("Enter your contact information: ")
    summary = input("Enter a brief summary about yourself: ")
    experience = input("Enter your work experience: ")
    education = input("Enter your education: ")
    skills = input("Enter your skills (comma-separated): ")

    create_resume(name, contact, summary, experience, education, skills)

    resume_text = f"{name}\n{contact}\n{summary}\n{experience}\n{education}\n{skills}"

    results = check_ats_friendly(resume_text)
    print("ATS Check Results:")
    for result in results:
        print(result)

    print("Your resume has been saved as 'resume.pdf'.")

if __name__ == "__main__":
    main()
