from mcp_server.utils.logger import logger
from fastmcp import FastMCP
from typing import Dict, Any
from mcp_server.data_models.example import ExampleToolRequest, ExampleToolResponse
from mcp_server.utils.request_wrapper import wrap_request_with_error_handling
import requests


class ExampleMCPServer:
    def __init__(self, config: Dict[str, Any]) -> None:
        logger.info(f"Initializing ExampleMCPServer with config: {config}")
        self.external_api_url = config["external_api_url"]

        self.mcp = FastMCP(
            name="ExampleMCPServer",
            instructions="""
            This server provides tools to interact with Cyrano, which generates posts
            based on ego personalities, post history, and sentiment.
            """,
            host=config["host"],
            port=int(config["port"]),
        )

        logger.info(f"FastMCP server created on {config['host']}:{config['port']}")
        self._register_tools()

    def _register_tools(self) -> None:
        logger.info("Start registering tools for ExampleMCPServer...")

        @self.mcp.tool(
            name="example_tool",
            description="Given an unsorted array of integers, returns the sorted array.",
        )
        def example_tool(request: ExampleToolRequest) -> ExampleToolResponse:
            sorted_array = sorted(request.array)
            return ExampleToolResponse(sorted_array=sorted_array)

        @self.mcp.tool(
            name="external_tool",
            description="Calls an external API with unsorted array and returns the sorted array.",
        )
        @wrap_request_with_error_handling
        def external_tool(request: ExampleToolRequest) -> ExampleToolResponse:
            logger.info(
                f"Calling external API at {self.external_api_url} with request: {request}"
            )
            response = requests.post(
                f"{self.external_api_url}/sort",
                json=vars(request),  # Convert Pydantic model to dict
            )
            response.raise_for_status()
            return ExampleToolResponse(**response.json())
