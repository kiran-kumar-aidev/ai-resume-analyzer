from pypdf import PdfReader

def extract_resume_text(pdf_file):
    reader = PdfReader(pdf_file)
    pages_text = []

    for page in reader.pages:
        text = page.extract_text()

        if text:
            pages_text.append(text)

    return "\n".join(pages_text)


