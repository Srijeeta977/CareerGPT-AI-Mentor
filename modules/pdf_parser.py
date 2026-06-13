from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_file):
    """
    Extract text from uploaded PDF resume
    """

    text = ""

    reader = PdfReader(pdf_file)

    for page in reader.pages:
        extracted = page.extract_text()

        if extracted:
            text += extracted + "\n"

    return text