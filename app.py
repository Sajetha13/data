# import pytesseract

# # Specify the path to Tesseract executable for Windows users
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# from pdf2image import convert_from_path

# # Function to extract text from PDF (certificate)
# def extract_text_from_pdf(pdf_path):
#     images = convert_from_path(pdf_path, poppler_path=r'C:\poppler-24.08.0\poppler-24.08.0\Library\bin')
#     text = ""
#     for img in images:
#         text += pytesseract.image_to_string(img)
#     return text

# # Function to extract text from an image (resume)
# def extract_text_from_image(img_path):
#     return pytesseract.image_to_string(img_path)

# # Example usage
# resume_text = extract_text_from_image("resume.png")
# certificate_text = extract_text_from_pdf("certificate.pdf")

# print("Resume Text:", resume_text)
# print("Certificate Text:", certificate_text)


# now for extraction into categories excel sheet

import pytesseract
from pdf2image import convert_from_path
import pandas as pd
import re

# Set the Tesseract executable path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Function to extract text from PDF (certificate)
def extract_text_from_pdf(pdf_path):
    images = convert_from_path(pdf_path, poppler_path=r'C:\poppler-24.08.0\poppler-24.08.0\Library\bin')
    text = ""
    for img in images:
        text += pytesseract.image_to_string(img)
    return text

# Extracting text from resume (or any image-based resume)
def extract_text_from_image(img_path):
    return pytesseract.image_to_string(img_path)

# Function to extract structured data from resume text
def extract_resume_data(resume_text):
    data = {
        'Name': None,
        'Age': None,
        'Caste': None,
        'Qualification': None,
        'Experience': None,
        'Skills': None,
        'Contact': None
    }

    # Example regex patterns for extraction
    name_pattern = r'Name:\s*(.*)'
    age_pattern = r'Age:\s*(\d+)'
    caste_pattern = r'Caste:\s*(.*)'
    qualification_pattern = r'Qualification:\s*(.*)'
    experience_pattern = r'Experience:\s*(.*)'
    skills_pattern = r'Skills:\s*(.*)'
    contact_pattern = r'Contact:\s*(.*)'

    # Search for patterns in the resume text
    data['Name'] = re.search(name_pattern, resume_text)
    data['Age'] = re.search(age_pattern, resume_text)
    data['Caste'] = re.search(caste_pattern, resume_text)
    data['Qualification'] = re.search(qualification_pattern, resume_text)
    data['Experience'] = re.search(experience_pattern, resume_text)
    data['Skills'] = re.search(skills_pattern, resume_text)
    data['Contact'] = re.search(contact_pattern, resume_text)

    # Extract and clean data
    for key in data:
        if data[key]:
            data[key] = data[key].group(1).strip()
        else:
            data[key] = 'Not Found'

    return data

# Example usage
resume_text = extract_text_from_image("resume.png")
certificate_text = extract_text_from_pdf("certificate.pdf")

# Extract structured data from resume
resume_data = extract_resume_data(resume_text)

# Create a DataFrame for both resume data and certificate text
df_resume = pd.DataFrame([resume_data])
df_certificate = pd.DataFrame({'Certificate Text': [certificate_text]})

# Save to Excel
output_file = "extracted_data.xlsx"
with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
    df_resume.to_excel(writer, sheet_name='Resume Data', index=False)
    df_certificate.to_excel(writer, sheet_name='Certificate Data', index=False)

print(f"Data extracted and saved to {output_file}")
