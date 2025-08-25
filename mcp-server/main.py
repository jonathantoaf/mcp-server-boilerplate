from mcp_server.utils.config import config
from mcp_server.mcp_server import MCPServer

# Initialize the MCP server with configuration
server = MCPServer(config["server"])
mcp = server.mcp

if __name__ == "__main__":
    # Start the MCP server
    mcp.run(transport=config["server"]["transport"], path="/mcp")
