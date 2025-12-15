# -*- coding: utf-8 -*-
from mcp.server.fastmcp import FastMCP 

# Create the FastMCP instance with stdio transport
mcp = FastMCP(name="weather", host="localhost", port=8002)

# Define the tool using the @mcp.tool() decorator
@mcp.tool()
def get_weather(city: str) -> str:
   """
   Returns weather of the city

   :param city: The city to get the weather for
   """
   return f"{city} weather is good"

# The tool is automatically added to the mcp instance by the decorator

# Run the server if the script is executed directly
if __name__ == "__main__":
   print("Starting [weather] MCP server...")
   # mcp.run(transport="stdio")
   # http 접근가능
   # mcp.run(transport="sse") 
   mcp.run()