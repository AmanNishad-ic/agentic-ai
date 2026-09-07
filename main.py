import streamlit as st
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import ChatPromptTemplate
from langchain_mistralai import ChatMistralAI
from langchain_core.output_parsers import StrOutputParser

# 1. Environment Variables Load Karein (.env file se HUGGINGFACEHUB_API_TOKEN)
load_dotenv()

# Page Title & Config
st.set_page_config(page_title="Simple english AI Assistant", page_icon="🤖", layout="centered")
st.title("🤖 Simple english AI Assistant")
st.caption("Aapka personal AI jo sab kuch simple English me samjhata hai.")

# 2. Model aur Chain ko Cache karein taaki har click par reload na ho
@st.cache_resource
def load_chain():
    model = ChatMistralAI(model= "ministral-8b-2512")

    prompt = ChatPromptTemplate.from_messages([
        ("system", "jo bhi mai tumko duga text tum use simple Einglish lnguage me samjoo ge. aur usame kya hai kaise hai ye bhi samjoo ge okya."),
        ("human", "{user_input}")
    ])
    
    # LCEL Chain setup
    return prompt | model | StrOutputParser()

chain = load_chain()

# 3. Chat History Maintain karne ke liye Session State
if "messages" not in st.session_state:
    st.session_state.messages = []

# 4. Old Chat History ko Screen par Render karein
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 5. User Input Field (ChatGPT Style)
if user_input := st.chat_input("Apna query ya text yahan likhein..."):
    
    # User message screen par dikhayein aur save karein
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # AI Response Generate karein
    with st.chat_message("assistant"):
        with st.spinner("Samajh raha hu..."):
            try:
                response = chain.invoke({"user_input": user_input})
                st.markdown(response)
                # Assistant response state me save karein
                st.session_state.messages.append({"role": "assistant", "content": response})
            except Exception as e:
                st.error(f"Error aaya hai: {e}")