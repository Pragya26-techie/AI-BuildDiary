from langchain_ollama import ChatOllama
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

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
prompt1 = template1.invoke({'topic':'black hole'})
result = model.invoke(prompt1)

prompt2 = template2.invoke({'text':result.content})
result1 = model.invoke(prompt2)

print(result1.content)


