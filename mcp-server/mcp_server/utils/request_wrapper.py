from typing import Callable, Any
from functools import wraps
from mcp_server.utils.logger import logger


def wrap_request_with_error_handling(
    request_func: Callable[..., Any],
) -> Callable[..., Any]:
    """
    A decorator for MCP tool functions that provides consistent error handling and logging.
    
    This decorator:
    - Catches and logs exceptions
    - Returns a standardized error response
    - Preserves function metadata
    
    Usage:
        @wrap_request_with_error_handling
        def my_tool(request: MyRequest) -> MyResponse:
            # Tool implementation
            pass
    """

    @wraps(request_func)
    def wrapper(*args, **kwargs) -> Any:
        try:
            result = request_func(*args, **kwargs)
            logger.debug(f"Successfully executed {request_func.__name__}")
            return result
        except Exception as e:
            logger.error(
                f"Error in {request_func.__name__}: {e}", exc_info=True
            )
            # Return a standardized error response
            return {
                "status": "error", 
                "message": str(e),
                "tool": request_func.__name__
            }

    return wrapper