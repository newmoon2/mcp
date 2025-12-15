# -*- coding: utf-8 -*-
import requests
from mcp.server.fastmcp import FastMCP

# Create the FastMCP instance with stdio transport
mcp = FastMCP(name="search", host="localhost", port=8001)

# Define the tool using the @mcp.tool() decorator
@mcp.tool()
def search_documents(search_text: str, search_type: str = "keyword", top_k: int = 3) -> str:
   """
   Returns search results

   :param search_text: The text to search for
   :param search_type: The type of search to perform. Defaults to 'keyword'.
   :param top_k: The number of top results to return. Defaults to 3.
   :return: The search results
   """
   print(f"search_text: {search_text}, search_type: {search_type}, top_k: {top_k}")
   try:
       payload = {
           "search_text": search_text,
           "search_type": search_type,
           "top_k": top_k
       }
       response = requests.post("http://localhost:8000/search", json=payload)
       response.raise_for_status()  # 4xx/5xx 응답 코드에 대해 예외를 발생시킵니다.
       return response.text
   except requests.exceptions.RequestException as e:
       return f"검색 중 오류가 발생했습니다: {e}"

# The tool is automatically added to the mcp instance by the decorator

# Run the server if the script is executed directly
if __name__ == "__main__":
   import uvicorn
   print("Starting [Search] MCP server...")
   # FastMCP의 내장 run() 메서드를 사용하여 HTTP 서버를 시작합니다.
   mcp.run()