from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")
st.header('Reasearch Tool')

paper_input = st.selectbox("Select Research Paper Name",["Attentiton is all you need","BERT:Pre-training of Deep Bidirectional Transformers","GPT-3:Language Models are Few-shot Learners","Diffusion Models Beat GANs on Image Synthesis"])

style_input = st.selectbox("Select Explanation Style",["Beginner-Friendly","Technical","Code-Oriented","Mathematical"])

length_input = st.selectbox("Select Explanation Length",["Short (1-2 paragraphs)","Medium (3-5 paragraphs)","Long(detailed explanation)"])

# designing prompt template
template = PromptTemplate(
    template = """
Please summarize the reasearch paper titled "{paper_input}" with following specifications:
Explanation Style:{style_input}
Explanation Length:{length_input}
1. Mathematical Details:
    - Include relevant mathematical equations if present in the paper.
    - Explain thd mathematical concepts using simple,intuitive code snippets where applicable.
2. Analogies:
    - Use reletable analogies to simplify complex ideas.
If certain information is not availabe in the paper,respond with:"Insufficient information available" instead of guessing.
Ensure the summary is clear,accurate,and aligned with the provided style and length,
""",
input_variables=['paper_input','style_input','lenth_input']
)

# fill the placeholder
prompt = template.invoke({
    'paper_input':paper_input,
    'style_input':style_input,
    'length_input':length_input
})


if st.button('Summarize'):
   result = model.invoke(prompt)
   st.write(result.content)
