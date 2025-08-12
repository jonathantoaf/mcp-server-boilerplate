from mcp_server.utils.config import config
from mcp_server.example_mcp_server import ExampleMCPServer

server = ExampleMCPServer(config["server"])
mcp = server.mcp

if __name__ == "__main__":
    mcp.run(transport=config["server"]["transport"], path="/mcp")
