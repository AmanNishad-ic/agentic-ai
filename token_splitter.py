from langchain_text_splitters import TokenTextSplitter, TextSplitter
from langchain_community.document_loaders import PyPDFLoader, TextLoader


loader = PyPDFLoader('Linear_Regression_Notes.pdf')

docs = loader.load()

splitter = TokenTextSplitter(
    chunk_size = 1000,
    chunk_overlap = 10
)

chunks = splitter.split_documents(docs)

print(chunks[0].page_content)