from starlette.requests import Request
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class McpSession:
    __session_manager: dict = {}

    @staticmethod
    def get_session(request: Request) -> dict:
        mcp_sesion_id: str | None = request.headers.get("mcp-session-id")
        if mcp_sesion_id and mcp_sesion_id not in McpSession.__session_manager:
            logger.info(f"init session: {mcp_sesion_id}")
            McpSession.__session_manager[mcp_sesion_id] = {}

        return McpSession.__session_manager[mcp_sesion_id]
