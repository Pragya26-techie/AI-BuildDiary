from langchain_ollama import ChatOllama
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatOllama(model = 'llama3.2:1b')
    
# 1st prompt -> detailed report
template1 = PromptTemplate(
    template='write a detailed report on {topic}',
    input_varibale=['topic']
)
# 2nd prompt -> summary
template2 =PromptTemplate(
        template = 'write a 5 line summary on the following text./n{text}',
        input_varibale = ['text']
                          )

parser = StrOutputParser()
chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({'topic':'black hole'})
print(result)
