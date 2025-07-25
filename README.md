We have three ways of transport with mcp. 
1. SSE (server sent events) - more suitable for remote connections.
2. stdio (usual way of communication, this is what will be used in default) - this is what we usually use for internal communication. This is more suitable if all the `client, server and host` are in the same local system.
3. streamable http - this is the recommended way, and will be the only supported way in the future.

`mcp run dev` - This command requires `mcp[cli]` to be installed on your computer. Use
**pip install mcp[cli]** to install it. This will install the MCP inspector. 

You can use it for the MCP server to run, and it will automcatically generate a session token as well. You can use it to authenticate requests, or you can bypass that check by using an environment variable `DANGEROUSLY_OMIT_AUTH=true`. This is dangerous as the name says.

The URL where you can access the console would look something like:
`http://localhost:<port>/?MCP_PROXY_AUTH_TOKEN=<token>`.

Once you see the console up, 
head to the transport type and choose `stdio`. Then in the command, use **uv**.
In the arguments section, provide **run --with mcp mcp run server.py**.

Then if you click on `list resources`, you will be able to list all the tools you made available to your server via the `@mcp.tool()` decorator.

In the resources section, you will be able to see the capabilities of the server.
In the tools section, you will be able to see the tool you exposed. It can be anything, but it is gonna be a python function with arguments. After this, you will be able to select the tools listed, where you will be able to provide inputs, if any, and then `run tool` button will execute the program.

Output looks something like:
{
  "type": "object",
  "properties": {
    "result": {
      "title": "Result",
      "type": "integer"
    }
  },
  "required": [
    "result"
  ],
  "title": "addOutput" // function name + "Output"
}


Capabilities include prompts, roots(directories) etc. We shall explore them as well.
