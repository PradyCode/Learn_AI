from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st

from langchain_core.prompts import PromptTemplate,load_prompt

load_dotenv()

model = ChatOpenAI()

st.header('Research Tool')
st.write('Check')
user_input = st.text_input('Enter Prompt Here')

if st.button('Summarize'):
    result = model.invoke(user_input)
    st.write(result.content)
