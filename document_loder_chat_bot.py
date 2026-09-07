from langchain_community.document_loaders import TextLoader,PyPDFLoader
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from langchain_core.prompts import ChatPromptTemplate
from langchain_text_splitters import CharacterTextSplitter
load_dotenv()

loder = PyPDFLoader('Linear_Regression_Notes.pdf')
docs = loder.load()
# print(docs)

llm = HuggingFaceEndpoint(
    repo_id= "deepseek-ai/DeepSeek-V4-Flash-0731"

)

model = ChatHuggingFace(llm=llm)
prompt = ChatPromptTemplate(

   [ ("system",'You are a AI that summarizes the text'),
    ("human","{document}")]

)

final_prompt = prompt.invoke(
    {'document': docs[1]}
)

responce = model.invoke(final_prompt)

print(responce.content)