from mcp_server.utils.logger import logger
from fastmcp import FastMCP
from typing import Dict, Any
from mcp_server.data_models.example import ExampleToolRequest, ExampleToolResponse, ExternalToolRequest, ExternalToolResponse
from mcp_server.utils.request_wrapper import wrap_request_with_error_handling
import requests


class MCPServer:
    """
    Generic MCP Server class that can be customized for different use cases.
    
    This class provides a foundation for building MCP servers with:
    - Configurable server settings
    - Tool registration system
    - Error handling
    - Logging
    """
    
    def __init__(self, config: Dict[str, Any]) -> None:
        logger.info(f"Initializing MCP Server with config: {config}")
        self.config = config
        self.external_api_url = config.get("external_api_url")

        self.mcp = FastMCP(
            name=config.get("name", "MCP Server"),
            instructions=config.get("instructions", "A generic MCP server."),
            host=config["host"],
            port=int(config["port"]),
        )

        logger.info(f"FastMCP server created on {config['host']}:{config['port']}")
        self._register_tools()

    def _register_tools(self) -> None:
        """Register all available tools with the MCP server."""
        logger.info("Registering tools for MCP Server...")

        # Example tool - replace with your own tools
        @self.mcp.tool(
            name="example_tool",
            description="Given an unsorted array of integers, returns the sorted array.",
        )
        def example_tool(request: ExampleToolRequest) -> ExampleToolResponse:
            sorted_array = sorted(request.array)
            logger.info(f"Sorted array: {request.array} -> {sorted_array}")
            return ExampleToolResponse(sorted_array=sorted_array)

        # Example external API tool - remove if not needed
        if self.external_api_url:
            @self.mcp.tool(
                name="external_tool",
                description="Given an unsorted array of integers, returns the sorted array from an external API.",
            )
            @wrap_request_with_error_handling
            def external_tool(request: ExternalToolRequest) -> ExternalToolResponse:
                logger.info(
                    f"Calling external API at {self.external_api_url} with request: {request}"
                )
                response = requests.post(
                    f"{self.external_api_url}/sort",
                    json=vars(request),
                    timeout=30
                )
                response.raise_for_status()
                return ExampleToolResponse(**response.json())

        logger.info("Tool registration completed")
