
# from mcp.server.fastmcp import FastMCP
# from typing import Dict

# mcp = FastMCP("math_server")

# @mcp.tool()
# async def calculate(expression: str) -> str:
#     """Evaluate a mathematical expression."""
#     try:
#         result = eval(expression, {"__builtins__": {}})
#         return str(result)
#     except Exception as e:
#         return f"Error: {str(e)}"

# if __name__ == "__main__":
#     mcp.run()

#######################
# from langchain_core.tools import tool

# @tool
# def calculate(expression: str) -> str:
#     """Evaluate a mathematical expression."""
#     try:
#         result = eval(expression, {"__builtins__": {}})
#         return str(result)
#     except Exception as e:
#         return f"Error: {str(e)}"