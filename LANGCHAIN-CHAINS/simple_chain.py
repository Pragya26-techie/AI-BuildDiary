from langchain_ollama import ChatOllama
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
prompt = PromptTemplate(
    template = 'Generate 5 interseting facts about {topic}',
    input_varibales = ['topic']
)

model = ChatOllama(model = 'llama3.2:1b')
parser = StrOutputParser()

chain = prompt | model | parser
result = chain.invoke({'topic':'Travelling'})
print(result)

# getting steps involved in chaining
chain.get_graph().print_ascii()