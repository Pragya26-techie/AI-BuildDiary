from langchain_ollama import ChatOllama
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
prompt1 = PromptTemplate(
    template = 'Generate a detailed report on  {topic}',
    input_varibales = ['topic']
)

prompt2 = PromptTemplate(
    template = " generate a 5 pointer sumaaary from the follwoing text \n {text}",
     input_varibales = ['text']
)
model = ChatOllama(model = 'llama3.2:1b')
parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser

result = chain.invoke({'topic':'unemployment in india'})
print(result)