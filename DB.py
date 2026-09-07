from langchain_mistralai import ChatMistralAI,MistralAIEmbeddings
from dotenv import load_dotenv
from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate          

load_dotenv()

model = ChatMistralAI(model= 'ministral-8b-2512')
embadding_model = MistralAIEmbeddings(model='mistral-embed')

vectorstore = Chroma(
    persist_directory= 'chrom-db',
    embedding_function= embadding_model
)

retrive = vectorstore.as_retriever(
        search_type = 'mrr',
        search_kwargs = {
        "k":4,
        "fetch_k":10,
        "lambda_mult" : 0.5
    }
)

prompt = ChatPromptTemplate.from_messages(
    [(
        "system",
        """You are a helpful AI assistant.

Use ONLY the provided context to answer the question.

If the answer is not present in the context,
say: "I could not find the answer in the document."
"""
    ),
    (
        "human",
        """Context:
{context}

Question:
{question}
"""
    )]
)

while True:
    quray = input("You: ")
    docs = retrive.invoke(quray)
    context = "\n\n".join([
        doc.page_content for doc in docs
    ])
    final_prompt = prompt.invoke({
        "context" : context,
        "question" : quray
    })
    responce = model.invoke(final_prompt)
    print(responce.content)





