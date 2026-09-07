from langchain_community.document_loaders import TextLoader

Loader = TextLoader('Linear_Regression_Notes.txt', encoding= 'utf-8')

docs = Loader.load()
print(docs)