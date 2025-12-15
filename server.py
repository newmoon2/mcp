# -*- coding: utf-8 -*-
from fastmcp import FastMCP 

mcp = FastMCP("search_documents")

@mcp.tool
def add(a: int, b:int) -> int:
    "add func"
    return a + b

if __name__ == "__main__":
    print("test-mcp-http")
    mcp.run(transport="http", host="0.0.0.0", port=8001)