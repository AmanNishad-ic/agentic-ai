from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader

splitter = CharacterTextSplitter(
    separator='',
    chunk_size = 10,
    chunk_overlap =1
)

loader = TextLoader('text.txt',encoding="utf-8")
doc = loader.load()
chunk = splitter.split_documents(doc)
for i in chunk:
    print(i.page_content)
    print()
    print()

