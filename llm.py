from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

def batch():
    chat = ChatGroq(temperature=0, model_name="mistral-saba-24b", groq_api_key=os.getenv("GROQ_API"))

    system = "You are a helpful assistant."
    human = "{text}"
    prompt = ChatPromptTemplate.from_messages([("system", system), ("human", human)])

    chain = prompt | chat
    print(chain.invoke({"text": "Explain the importance of low latency LLMs."}))

# Streaming
def streaming():
    chat = ChatGroq(temperature=0, model_name="llama3-70b-8192",groq_api_key=os.getenv("GROQ_API"))
    prompt = ChatPromptTemplate.from_messages([("human", "Write a very long poem about {topic}")])
    chain = prompt | chat
    for chunk in chain.stream({"topic": "The Moon"}):
        print(chunk.content, end="", flush=True)

# batch()
streaming()