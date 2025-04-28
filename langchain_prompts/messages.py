
# There are three kinds of messages in Langchain
# System, AI and Human

from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI

from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

messages = [
    SystemMessage(content= "You are a helpful financial assistant who is an expert in financial models"),
    HumanMessage(content= "I am an investor concered about the trade war that Trump invoked and it's affect on the market, how should i got about distributing my portfolio and what are some of the compaines who will win here?")
]

result = model.invoke(messages)

messages.append(AIMessage (content=result.content))

print(messages)
