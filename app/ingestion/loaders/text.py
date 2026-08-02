import logfire

def parse_text(file_path: str):
    """
    Parses plain text files.
    """
    with logfire.span("TEXT PARSING", filename=file_path):
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                return f.read()
        except Exception as e:
            logfire.error(f"TEXT PARSING FAILED WITH ERROR: {e}")
            raise e