from langchain_mistralai import MistralAIEmbeddings
from dotenv import load_dotenv
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import  Chroma

load_dotenv()

loader = PyPDFLoader('Linear_Regression_Notes.pdf')

docs = loader.load()

model = MistralAIEmbeddings(model='mistral-embed')

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap = 1
)

chunks = splitter.split_documents(docs)

vector_store = Chroma.from_documents(
    documents= chunks,
    embedding= model,
    persist_directory="chrom-db"
)