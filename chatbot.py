from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3.8-flash")

chat_history = [
    SystemMessage(content='You are a helpful AI assistant')
]

while True:
    user_input = input('You: ')
    if user_input == 'exit':
            break
    chat_history.append(HumanMessage(content=user_input))
    
    result = model.invoke(chat_history)

    ai_response = result.content[0]["text"]
    chat_history.append(result)
    print("AI:",ai_response)

print(chat_history)