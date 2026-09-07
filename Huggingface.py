from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import  load_dotenv
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id= "deepseek-ai/DeepSeek-V4-Flash-0731",
)

model = ChatHuggingFace(llm = llm)
responce = model.invoke('who are you?')
print(responce.content)