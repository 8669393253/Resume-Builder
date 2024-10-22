# Resume-Builder
A simple command-line application to create an ATS-friendly resume in PDF format. This project allows users to input their personal information, work experience, education, and skills, and generates a well-structured resume.

## Features
**PDF Generation**: Create a professional-looking resume in PDF format using the `FPDF` library.
**Text Sanitization**: Automatically replaces special characters to ensure proper formatting in the PDF.
**ATS Compatibility Check**: Analyzes the resume for common ATS issues, such as missing sections and keyword presence.

## Requirements
- Python 3.x
- `fpdf` library

## Installation
1. Clone the repository:
   git clone https://github.com/yourusername/resume-builder.git
   cd resume-builder

2. Install the required library:
   pip install fpdf

## Usage

1. Run the script:
   python resume_builder.py
   
3. Follow the prompts to enter your details:

   - Name
   - Contact information
   - Brief summary
   - Work experience
   - Education
   - Skills (comma-separated)

4. After entering all details, a PDF resume will be generated and saved as `resume.pdf`.

5. The program will also perform an ATS compatibility check and display the results.

## Example
Welcome to the Resume Builder!
Enter your name: John Doe
Enter your contact information: john.doe@example.com
Enter a brief summary about yourself: Experienced software developer...
Enter your work experience: Software Engineer at XYZ Corp...
Enter your education: B.S. in Computer Science...
Enter your skills (comma-separated): Python, Java, Teamwork...

## ATS Check Results

The program will provide feedback on your resume's ATS compatibility, highlighting areas for improvement.

## Contributing

Feel free to submit issues or create pull requests if you have suggestions for improvements or new features!

## Notes:
- Be sure to replace `yourusername` with your actual GitHub username in the clone URL.
- You can modify any sections based on your specific project requirements or personal preferences.
- Add any additional details you think would help users understand and use your project effectively!
