from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(model = 'gemini-3.8-flash')

parser = JsonOutputParser()

# prompt template
template = PromptTemplate(
    template = "Give me the name,age and city of a fictional person \n{format_instruction}",
    input_variables = [],
    partial_variables = {'format_instruction':parser.get_format_instructions()}
)

# disadvantage of using jsonouput parser it gives output in its own structure
template2 = PromptTemplate(
    template = "Give me 5 facts baout {topic} \n{format_instruction}",
    input_variables = ['topic'],
    partial_variables = {'format_instruction':parser.get_format_instructions()}
)

# using chianing method
chain = template | model | parser
result = chain.invoke({})
print(result)

chain2 = template2 | model | parser
result1 = chain.invoke({'topic':'black hole'})
print(result1)

# older method
# prompt = template.format()
# result = model.invoke(prompt)
# final_result = parser.parse(result.content[0]['text'])
# print(final_result)
# print(type(final_result))
