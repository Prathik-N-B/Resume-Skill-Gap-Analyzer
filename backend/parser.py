import pymupdf


def extract_text_from_pdf(file):
    data = file.read()
    if not data:
        raise ValueError("The uploaded file is empty.")

    try:
        with pymupdf.open(stream=data, filetype="pdf") as pdf:
            if pdf.page_count == 0:
                raise ValueError("The PDF has no pages.")

            text = "\n".join(page.get_text() for page in pdf)
    except pymupdf.FileDataError as error:
        raise ValueError("The uploaded file is not a valid PDF.") from error

    if not text.strip():
        raise ValueError(
            "No selectable text found. Scanned PDFs are not supported yet."
        )

    return text