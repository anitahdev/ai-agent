from dotenv import load_dotenv 
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic

load_dotenv()

llm = ChatAnthropic(model="claude-3-5-sonnet-20241022")
response = llm.invoke("How to make banana bread? ")
print(response)