from langchain_mistralai import MistralAIEmbeddings
from dotenv import load_dotenv
load_dotenv()
embedding = MistralAIEmbeddings(
    model= 'mistral-embed',
    dimensions= 64
)

vector = embedding.embed_query('your are going to lear gen ai')
print(vector)

'''-------------------------------------------------------------------------------'''

# from langchain_mistralai import MistralAIEmbeddings
# from dotenv import load_dotenv

# load_dotenv()

# embedding = MistralAIEmbeddings(
#     model="mistral-embed",
    
# )

# vector = embedding.embed_query(
#     "you are going to learn Gen AI"
# )

# print(vector)