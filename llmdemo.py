from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model='gpt-4', temperature=0.7, max_tokens=100)

result = model.invoke("who is prime minister of India?")

print(result)


for lab testing 
