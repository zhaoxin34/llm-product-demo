import logging
import contextlib
from mcp.server.fastmcp import FastMCP
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.applications import Starlette
from starlette.routing import Mount
from typing import AsyncIterator
from contextlib import asynccontextmanager
from server.server_context import ServerContext

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(_) -> AsyncIterator[ServerContext]:
    """Manage application lifecycle with type-safe context."""
    # 可通过ctx.request_context.lifespan_context 访问到
    data = "initial a new value"
    yield ServerContext(data=data)


class RequestLoggerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        logger.info(f"Request: {request.method} {request.url.path}")
        response = await call_next(request)
        logger.info(f"Response: {response.status_code}")
        return response


# Create MCP server instance
mcp = FastMCP(
    "DataAnalytics MCP", stateless_http=False, json_response=True, lifespan=lifespan
)


# Create a lifespan context manager to run the session manager
@contextlib.asynccontextmanager
async def app_lifespan(_: Starlette):
    async with mcp.session_manager.run():
        yield


# Mount using Host-based routing
app = Starlette(
    routes=[
        Mount("/", app=mcp.streamable_http_app()),
    ],
    lifespan=app_lifespan,
)

# app.add_middleware(RequestLoggerMiddleware)
