from typing import List
from langchain_text_splitters import RecursiveCharacterTextSplitter
import logfire

def chunk_text(text: str, chunk_size: int = 1500, chunk_overlap: int = 200) -> List[str]:
    with logfire.span("TEXT CHUNKING", text_length=len(text)):
        if not text.strip():
            return []
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            separators=[
                "\n\n", #paragraph
                "\n", #line
                ". ", #sentence
                " ", #word
                "" #character
            ]
        )
        chunks = splitter.split_text(text)
        logfire.info(f"Successfully Generated {len(chunks)} chunks")
        return chunks