import asyncio

from mcp.types import CallToolResult
import pytest
from mcp import ClientSession
from mcp.client.streamable_http import streamable_http_client
from src.service.segment_service import ensure_segment_name_unique


@pytest.mark.asyncio
async def test_app():
    # Connect to a streamable HTTP server
    async with streamable_http_client("http://localhost:8000/mcp") as (
        read_stream,
        write_stream,
        _,
    ):
        # Create a session using the client streams
        async with ClientSession(read_stream, write_stream) as session:
            # Initialize the connection
            await session.initialize()
            # List available tools
            tools = await session.list_tools()
            print(f"Available tools: {[tool.name for tool in tools.tools]}")

            result: CallToolResult = await session.call_tool("login", {})
            assert not result.isError
            print(result.content)

            result = await session.call_tool("query_segment_list", {"name": "自定义"})
            assert not result.isError
            print(result.content)

            result = await session.call_tool(
                "ensure_segment_name_unique", {"name": "自定义"}
            )
            assert not result.isError
            print(result.content)

            result = await session.call_tool("save_segment", {"name": "自定义"})
            assert not result.isError
            print(result.content)
