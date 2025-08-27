from envyaml import EnvYAML
from mcp_server.data_models.config import MCPServerConfig

config = EnvYAML("mcp_server/config.yaml", strict=False)
server_config = MCPServerConfig(**config["server"])
