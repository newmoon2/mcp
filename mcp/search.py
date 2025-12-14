# -*- coding: utf-8 -*-
import requests
from mcp.server.fastmcp import FastMCP # Parameter is not strictly needed now, but good practice to keep if you add more complex params later

# Create the FastMCP instance with stdio transport
mcp = FastMCP()

# Define the tool using the @mcp.tool() decorator
@mcp.tool()
def get_search(search_text: str, search_type: str = "keyword", top_k: int = 3) -> str:
   """
   Returns search results

   :param search_text: The text to search for
   :param search_type: The type of search to perform. Defaults to 'keyword'.
   :param top_k: The number of top results to return. Defaults to 3.
   :return: The search results
   """
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
   print("Starting MCP server...")
   mcp.run(transport="stdio")