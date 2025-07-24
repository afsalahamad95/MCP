from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv

env = load_dotenv(".env")

server = FastMCP(
	name="simple-mcp-calculator-server",
	host="0.0.0.0", # for sse transport
	port=9000,
)

# we create a tool on the above server
@server.tool()
def add(a: int, b: int) -> int:
	return a + b

def main():
	server.run(transport="stdio") # can use sse alternatively, but it is deprecated.