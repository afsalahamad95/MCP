from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv

env = load_dotenv(".env")

mcp_server = FastMCP(
	name="simple-mcp-calculator-server",
	host="0.0.0.0", # for sse transport
	port=9000,
)

# we create a tool on the above server
@mcp_server.tool()
def add(a: int, b: int) -> int:
	return a + b