import logfire
from unstructured.partition.auto import partition

def parse_office(file_path: str):
    """
    Parses Office documents (.docx, .pptx) using the Unstructured library.
    """
    with logfire.span("OFFICE DOCUMENT PARSING", filename=file_path):
        try:
            # Unstructured automatically detects if it's docx or pptx
            elements = partition(filename=file_path)
            full_text = "\n".join([str(el) for el in elements])
            if not full_text.strip():
                logfire.warning(f"Unstructured returned empty text for {file_path}")
            else:
                logfire.info(f"Successfully parsed {len(full_text)} characters")
            return full_text
        except Exception as e:
            logfire.error(f"OFFICE PARSING FAILED WITH AN ERROR: {e}")
            raise e