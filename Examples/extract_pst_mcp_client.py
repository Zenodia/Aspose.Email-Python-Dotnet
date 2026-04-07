import asyncio
import sys
from fastmcp import Client
from colorama import Fore, init

init(autoreset=True)

MCP_SERVER_URL = "http://localhost:9003/mcp"

def stream_print(text: str):
    """Print text word-by-word to simulate streaming output."""
    words = text.split(" ")
    for i, word in enumerate(words):
        print(Fore.GREEN + word, end="" if i == len(words) - 1 else " ", flush=True)
    print()  # final newline


async def call_pst_agent(query: str) -> str:
    async with Client(MCP_SERVER_URL) as client:
        result = await client.call_tool("pst_agent", {"query": query})
    return result.content[0].text


query = input(Fore.YELLOW + "What would you like to do?\n> ").strip()

try:
    output = asyncio.run(call_pst_agent(query))
except Exception as e:
    print(Fore.RED + f"Error calling MCP server: {e}")
    sys.exit(1)

print("\n")
print(Fore.CYAN + "Result: ", end="")
stream_print(output)
