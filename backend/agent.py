from langchain_openai import ChatOpenAI
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver
from math_tool import calculate
from dotenv import load_dotenv
import os

load_dotenv()

# Initialize the LLM
model = ChatOpenAI(model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"))

#tool wrappers
api_wrapper = WikipediaAPIWrapper()
wikipedia_tool = WikipediaQueryRun(api_wrapper=api_wrapper)

async def create_graph():
    """Create and return a LangGraph agent with built-in tools."""
    tools = [DuckDuckGoSearchRun(),wikipedia_tool]  # built-in tools
    memory = MemorySaver()
    agent = create_react_agent(model, tools, checkpointer=memory)
    return agent

# from langchain_openai import ChatOpenAI
# from langchain_mcp_adapters.client import MultiServerMCPClient
# from langgraph.prebuilt import create_react_agent
# from langgraph.checkpoint.memory import MemorySaver
# from dotenv import load_dotenv
# import os

# load_dotenv()

# model = ChatOpenAI(model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"))

# async def create_graph():
#     client = MultiServerMCPClient({
#         "math": {
#             "command": "python",
#             "args": ["math_server.py"],
#             "transport": "stdio",
#         }
#     })
#     tools = await client.get_tools()
#     memory = MemorySaver()
#     agent = create_react_agent(model, tools, checkpointer=memory)
#     return agent, client  # Return client for cleanup if needed