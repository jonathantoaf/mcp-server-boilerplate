from mcp_server.utils.config import server_config
from mcp_server.mcp_server import MCPServer

# Initialize the MCP server with configuration
server = MCPServer(server_config)
mcp = server.mcp

if __name__ == "__main__":
    # Start the MCP server
    mcp.run(transport=server_config.transport, path="/mcp")
