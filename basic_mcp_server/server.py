from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
import os

load_dotenv(".env")

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
	serverTransport = os.getenv("TRANSPORT")
	print(f"transport: {serverTransport}")
	if serverTransport == "sse":
		server.run(transport="sse") 
	elif serverTransport == "stdio":
		server.run(transport="stdio") 
	else:
		server.run(transport="streamableHttp") 

if __name__ == "__main__":
	main()