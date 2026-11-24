from langchain_ollama import ChatOllama
from dotenv import load_dotenv
from typing import TypedDict

load_dotenv()

model = ChatOllama(model = 'llama3.2:1b')

#schems
class Review(TypedDict):
    sumarry: str
    sentiment: str

structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""The hardware is great,but the sofare feels bloated.There are too  many pre-installed apps that ican't remove.Also the uI looks outdatedd compare to other brands.Hoping for a software update to fix this.""")
print(result['summary'])
print(result['sentiment'])