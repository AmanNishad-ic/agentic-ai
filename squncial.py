from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory
import edge_tts
import asyncio
import speech_recognition as sr
from dotenv import load_dotenv
import os
.
# Load environment (agar HuggingFace API key .env me rakhi ho)
load_dotenv()

# HuggingFace model
llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V4-Flash-0731",
    task="text-generation"
)
chat_model = ChatHuggingFace(llm=llm)

# Prompt with memory placeholder
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Answer in hinglish  language.and your name Jarvis and your sir aman aur tum ko aman sir ne banaya hai aur tum unki help ke liye bani ho. bina aman sir ejajt ke bina apna name mat change krna.jab stop bola jaye tum tum kucch bhi mat bolna "),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}")
])

# Combine prompt + model
chain = prompt | chat_model

# Store sessions
store = {}

def get_history(session_id: str):
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]

# Runnable with history
conversations = RunnableWithMessageHistory(
    chain,
    get_history,
    input_messages_key="input",
    history_messages_key="history",
)

# edge-tts voice output (Only Hindi)
async def speak(text: str):
    voice = "hi-IN-SwaraNeural"  # ✅ Hindi voice
    tts = edge_tts.Communicate(text, voice=voice)
    filename = "response_hi.mp3"
    await tts.save(filename)
    os.system(f"start {filename}")  # Windows ke liye

# Main chatbot loop

def cmd(user_input):
    
   
    
    response = conversations.invoke(
        {"input": user_input},
        config={"configurable": {"session_id": "aman"}}
    )

    print("Bot:", response.content)
    # ✅ Hindi bolne ke liye
    asyncio.run(speak(response.content))
        

# def rec():
#     while True:
#         r = sr.Recognizer()
#         try:
#             with sr.Microphone() as source:
#                 print("Listing...") 
                
#                 audio = r.listen(source)
#                 print("recognizing....")
#                 command = r.recognize_google(audio)
#             if (command.lower()=="Jarvis"):
#                 print("Active Jarvis...")
#                 with sr.Microphone() as source:
#                     print("Listing...") 
                    

#             print(command)
#         except sr.UnknownValueError:
#             print("muje samaj nahi aaya..")
#         cmd(command)
# rec()


def rec():
    r = sr.Recognizer()
    while True:
        try:
            with sr.Microphone() as source:
                print("Say 'Jarvis' to activate...")
                audio = r.listen(source)
                command = r.recognize_google(audio)
            
            # Agar Jarvis bola gaya to hi activate hoga
            if command.lower() == "jarvis":
                print("You said:", command)
                print("Jarvis Active... Listening for your command...")
                
                # for i in "jarvis":
                #     i = "Jarvis Active... Listening for your command..."
                #     print(i)
                try:
                    with sr.Microphone() as source:
                        audio = r.listen(source)
                        real_command = r.recognize_google(audio)
                        # if "Jarvis" in real_command.lower():
                        print("Your command:", real_command)
                        cmd(real_command)  # Ab sirf Jarvis ke baad command chalega
                except sr.UnknownValueError:
                    print("Mujhe samajh nahi aaya...")  # Sirf active hone ke baad print
                    jarvis_active = True  # Command ke baad phir se inactive

        except sr.UnknownValueError:
            # Agar Jarvis inactive hai → kuch bhi print na ho
            if jarvis_active:
                print("Mujhe samajh nahi aaya...")

# def cmd(command):
#     print("Executing:", command)  # yaha aap apna logic laga sakte ho

rec()
