from typing import Callable, Any
from functools import wraps
from mcp_server.utils.logger import logger


def wrap_request_with_error_handling(
    request_func: Callable[..., Any],
) -> Callable[..., Any]:
    """
    A decorator for MCP tool functions that make HTTP requests and want consistent error handling/logging.
    """

    @wraps(request_func)
    def wrapper(*args, **kwargs) -> Any:
        try:
            return request_func(*args, **kwargs)
        except Exception as e:
            logger.error(
                f"HTTP request error in {request_func.__name__}: {e}", exc_info=True
            )
            return {"status": "error", "message": str(e)}

    return wrapper
