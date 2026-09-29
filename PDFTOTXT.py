from pypdf import PdfReader
import os

pdf_folder = "Calendars"
text_folder = "Text Files"

os.chdir(pdf_folder)

pdfs = os.listdir()

for pdf in pdfs:
    
    file_name, file_type = os.path.splitext(pdf)
    reader = PdfReader(pdf)
    page = reader.pages[0]
    text = page.extract_text()
    
    output_path = os.path.join(text_folder, f"{file_name}.txt")
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)
    