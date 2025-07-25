import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def main():
	server_params = StdioServerParameters(
		command="python",
		args=["server.py"],
	)

	# connect to server
	async with stdio_client(server_params) as (read_stream, write_stream):
		async with ClientSession(read_stream, write_stream) as session:
			await session.initialize()

			# get tools
			tools = await session.list_tools()
			for tool in tools:
				print(f"tool available: {tool.name} -> {tool.description}")
			
			tool_name = "add"
			calculator = tools[tool_name]
			print(f"tool: {calculator.name} -> {calculator.description}")

			# call tool
			result = await session.call_tool(tool_name, 1, 2)
			print(f"result: {result}")

if __name__ == "__main__":
	asyncio.run(main())