import asyncio
from mcp import ClientSession
from mcp.client.sse import sse_client

async def main():
	async with sse_client("http://localhost:9000/sse") as (read_stream, write_stream):
		async with ClientSession(read_stream, write_stream) as session:
			await session.initialize()

			# get tools
			tools = await session.list_tools()
			for tool in tools:
				print(f"tool available: {tool.name} -> {tool.description}")
				
			result = await session.call_tool("add", arguments={"a": 1, "b": 2})
			print(f"result: {result.content}")

if __name__ == "__main__":
	asyncio.run(main())