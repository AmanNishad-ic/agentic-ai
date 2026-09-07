from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("Linear_Regression_Notes.pdf")
docs = loader.load()
splitter = RecursiveCharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap = 1
)

chunks = splitter.split_documents(docs)