from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model = 'gpt-4',temperature= 0.5, max_completion_tokens= 1000)

result = model.invoke("Where is the best place to rent in new york?")

print(result.content)