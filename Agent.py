from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id= "deepseek-ai/DeepSeek-V4-Flash-0731"
)
model = ChatHuggingFace(llm=llm)

prompt = ChatPromptTemplate(
    [('system',"You are a personal AI assistant created by Aman | your name is jaira | you are toking in hinglish language | you are only personal AI assistant of Aman not any one. "),
    ('human','{Human_interection}')]
)

while True:
    user = input("You: ")
    final_prompt = prompt.invoke({
        "Human_interection":user
    })

    responce = model.invoke(final_prompt)
    print(responce.content)
    