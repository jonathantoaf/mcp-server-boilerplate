import logging
import logging.config
from mcp_server.utils.config import config

logging.config.dictConfig(config["logging"])
logger = logging.getLogger("mcp-server")
