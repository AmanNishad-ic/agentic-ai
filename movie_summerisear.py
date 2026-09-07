from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel
from typing import List, Optional
from dotenv import load_dotenv

load_dotenv()

model = ChatMistralAI(
    model = 'mistral-small-2603'
)

class Movie(BaseModel):
    title: str
    release_year: Optional[int] = None
    genre: List[str]
    director: Optional[str] = None
    rating: Optional[float] = None
    cost : list[str]
    summary: str

parser = PydanticOutputParser(pydantic_object=Movie)


prompt = ChatPromptTemplate.from_messages(
    [('system','''Extract movie information from the paragraph {formet_instrection}'''),
    ("human", "{paragraph}")]
)

pars = input("Given your Paragarph : ")

final_prompt = prompt.invoke({
    "paragraph": pars,
    "formet_instrection": parser.get_format_instructions()
})

responce = model.invoke(final_prompt)

print(responce.content)