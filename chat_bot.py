from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage,SystemMessage,HumanMessage
from dotenv import load_dotenv

load_dotenv()

def chat_bot():
    model = ChatMistralAI(
        model = 'ministral-8b-2512',
        max_tokens= 500
    )
    choice = input('''
            ------- Select  your mode-------------
            For said - 1
            for funny - 2
            for happy - 3
    you: ''')
    if choice == "1":
        choice = 'said'
    elif choice == "2":
        choice = 'funny' 
    elif choice == "3":
        choice = 'Happy'
    else:
        print("wrong mode")

    message = [
        SystemMessage(content=f'{choice}, your name is jaira, tum sirf hienglish language me bat krna okya.')
    ]

    while True:
        a = input("You :")
        message.append(HumanMessage(content=a))
        reaponce = model.invoke(message)
        result = reaponce.content
        message.append(AIMessage(content=result))
        print(result)

if __name__ == "__main__":
    chat_bot()