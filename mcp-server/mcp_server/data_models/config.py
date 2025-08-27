from pydantic import BaseModel, Field


class MCPServerConfig(BaseModel):
    host: str = Field(description="Host address for the MCP server")
    port: int = Field(description="Port number for the MCP server")
    transport: str = Field(description="Transport protocol for the MCP server")
    name: str = Field(description="Name of the MCP server")
    instructions: str = Field(
        default=None, description="Instructions for using the MCP server"
    )
    external_api_url: str = Field(
        default=None, description="External API URL for the MCP server"
    )
