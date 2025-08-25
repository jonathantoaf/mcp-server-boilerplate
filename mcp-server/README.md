# MCP Server Boilerplate

A simple and generic starting point for building Model Context Protocol (MCP) servers using FastMCP.

## Features

- 🚀 **FastMCP Integration**: Built on the FastMCP framework for easy MCP server development
- 📁 **Organized Structure**: Clean, modular codebase with separation of concerns
- 🔧 **Configuration Management**: YAML-based configuration with environment variable support
- 📝 **Logging**: Structured logging with colored console output
- 🐳 **Docker Ready**: Includes Dockerfile for containerization
- 🛠️ **Developer Tools**: Pre-configured with Ruff for linting and formatting
- 📦 **UV Package Manager**: Fast dependency management with uv

## Quick Start

### Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) (recommended) or pip

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd mcp-server-boilerplate/mcp-server
   ```

2. **Install dependencies**
   ```bash
   # Using uv (recommended)
   uv sync

   # Or using pip
   pip install -e .
   ```

3. **Configure your server**
   ```bash
   # Copy the example environment file
   cp .env.example .env
   
   # Edit the .env file with your settings
   vim .env
   ```

4. **Run the server**
   ```bash
   # Using uv
   uv run python main.py

   # Or using python directly (after activating venv)
   python main.py
   ```

## Project Structure

```
mcp-server/
├── main.py                          # Entry point
├── pyproject.toml                   # Project configuration
├── dockerfile                      # Docker configuration
├── setup.py                        # Development setup script
├── .env.example                    # Example environment variables
├── mcp_server/
│   ├── config.yaml                 # Server configuration
│   ├── mcp_server.py                # Main MCP server class
│   ├── data_models/                # Pydantic models
│   │   ├── base.py                 # Base model with common config
│   │   └── example.py              # Example tool request/response models
│   └── utils/                      # Utility modules
│       ├── __init__.py             # Package init
│       ├── config.py               # Configuration loader
│       ├── logger.py               # Logging setup
│       └── request_wrapper.py      # Error handling decorators
```

## Creating Your MCP Server

### 1. Define Your Tools

Create request/response models in `mcp_server/data_models/example.py` or create new model files:

```python
from mcp_server.data_models.base import SharedBaseModel
from pydantic import Field

class MyToolRequest(SharedBaseModel):
    input_text: str = Field(description="Text to process")

class MyToolResponse(SharedBaseModel):
    result: str = Field(description="Processed result")
```

### 2. Implement Your Server

Modify `mcp_server/mcp_server.py` to add your tools to the `MCPServer` class:

```python
@self.mcp.tool(
    name="my_tool",
    description="Description of what your tool does"
)
def my_tool(request: MyToolRequest) -> MyToolResponse:
    # Your tool logic here
    result = process_text(request.input_text)
    return MyToolResponse(result=result)
```

### 3. Configure Your Server

Update `.env` file with your specific settings:

```bash
SERVER_NAME="Your MCP Server"
SERVER_INSTRUCTIONS="Description of your server's capabilities"
HOST=0.0.0.0
PORT=5000
```

## Configuration

The server uses environment variables that can be set in `.env` file:

- `HOST`: Server host (default: "0.0.0.0")
- `PORT`: Server port (default: "5000")
- `TRANSPORT`: Transport type (default: "streamable-http")
- `LOG_LEVEL`: Logging level (default: "DEBUG")
- `SERVER_NAME`: Name of your MCP server
- `SERVER_INSTRUCTIONS`: Description of your server's capabilities
- `EXTERNAL_API_URL`: URL for external API calls (if needed)

## Docker Deployment

Build and run with Docker:

```bash
# Build the image
docker build -t my-mcp-server .

# Run the container
docker run -p 5000:5000 --env-file .env my-mcp-server
```

## Development

### Setup Development Environment

```bash
# Run the automated setup
python setup.py
```

### Code Quality

```bash
# Format code
uv run ruff format

# Lint code
uv run ruff check

# Fix linting issues
uv run ruff check --fix
```


## Example Tools

The boilerplate includes example tools that demonstrate:

1. **Simple Tool**: `example_tool` - Sorts an array of integers
2. **External API Tool**: `external_tool` - Calls an external API to sort an array

You can find these in `mcp_server/mcp_server.py` and use them as templates for your own tools.

## Customization Guide

1. **Rename the project**: Update `pyproject.toml` name and description
2. **Add your tools**: Implement tools in the `MCPServer` class in `mcp_server.py`
3. **Configure environment**: Update `.env` with your specific settings
4. **Add dependencies**: Update `pyproject.toml` dependencies section
5. **Customize models**: Create new models in `data_models/` or modify existing ones

## Error Handling

The boilerplate includes error handling decorators:

```python
from mcp_server.utils.request_wrapper import wrap_request_with_error_handling

@wrap_request_with_error_handling
def my_api_tool(request: MyRequest) -> MyResponse:
    # Your API call logic here
    pass
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request


## Resources

- [FastMCP Documentation](https://github.com/jlowin/fastmcp)
- [Model Context Protocol Specification](https://modelcontextprotocol.io/)
- [Pydantic Documentation](https://docs.pydantic.dev/)