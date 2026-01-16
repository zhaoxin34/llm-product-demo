import pytest
from unittest.mock import MagicMock
from mcp.server.session import ServerSession

from mcp.shared.memory import (
    create_connected_server_and_client_session as client_session,
)
from app import mcp


@pytest.mark.asyncio
async def test_login():
    async with client_session(mcp._mcp_server) as client:
        result = await client.call_tool("login", {})
        # print(result)
