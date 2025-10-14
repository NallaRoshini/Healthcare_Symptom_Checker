from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.schema import HumanMessage, SystemMessage
import os

load_dotenv()

# Initialize Groq client through LangChain wrapper
llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name=os.getenv("GROQ_MODEL", "llama-3.1-8b-instant")
)

async def query_llm(messages):
    """Query Groq Llama model using LangChain ChatGroq."""
    from concurrent.futures import ThreadPoolExecutor
    import asyncio

    # Convert message dicts into LangChain messages
    chat_messages = []
    for msg in messages:
        if msg["role"] == "system":
            chat_messages.append(SystemMessage(content=msg["content"]))
        elif msg["role"] == "user":
            chat_messages.append(HumanMessage(content=msg["content"]))

    # Run synchronously within async FastAPI
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        response = await loop.run_in_executor(pool, lambda: llm.invoke(chat_messages))

    return response.content
