#!/usr/bin/env python3
"""
示例mcp，直接使用python deom.py即可启动
"""

import json
import logging
import contextlib
from datetime import datetime

from mcp.server.fastmcp import Context, FastMCP
from starlette.applications import Starlette
from starlette.routing import Mount
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request

from mcp_session import McpSession

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class RequestLoggerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        logger.info(f"Request: {request.method} {request.url.path}")
        response = await call_next(request)
        logger.info(f"Response: {response.status_code}")
        return response


# Create MCP server instance
mcp = FastMCP("DataAnalytics MCP", stateless_http=False, json_response=True)


@mcp.tool()
async def get_system_status(ctx: Context) -> str:
    """
    Get the current system status.

    Returns:
        System status information
    """
    status = {
        "status": "healthy",
        "services": {
            "api": "running",
            "database": "running",
            "analytics": "running",
            "cache": "running",
        },
        "uptime": "24h 15m",
        "memory_usage": "67%",
        "cpu_usage": "34%",
        "last_check": datetime.now().isoformat(),
        "version": "1.0.0",
    }

    return json.dumps(status, indent=2)


@mcp.tool()
async def get_session(ctx: Context) -> str:
    """
    Test the session

    Returns:
        A Session
    """
    try:
        session = McpSession.get_session(ctx.request_context.request)
        counter = session.get("counter", 1)
        session["counter"] = counter + 1
        return f"counter: {counter}"
    except Exception as e:
        return f"发生错误: {e}"


# Create a lifespan context manager to run the session manager
@contextlib.asynccontextmanager
async def lifespan(app: Starlette):
    async with mcp.session_manager.run():
        yield


# Mount using Host-based routing
app = Starlette(
    routes=[
        Mount("/", app=mcp.streamable_http_app()),
    ],
    lifespan=lifespan,
)
app.add_middleware(RequestLoggerMiddleware)

if __name__ == "__main__":
    # Run the MCP server
    logger.info("Starting DataAnalytics MCP Server...")
    # mcp.run(transport="streamable-http")
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
