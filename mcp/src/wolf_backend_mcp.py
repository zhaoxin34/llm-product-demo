#!/usr/bin/env python3
"""
wolf 后端 mcp
"""

import logging
import json
from fastmcp import FastMCP
from service import login_service

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create MCP server instance
mcp = FastMCP("wolf 后端 MCP", stateless_http=False, json_response=True)


@mcp.tool()
async def login() -> str:
    """
    登录到wolf系统

    Returns:
        登录用户的信息
    """
    return json.dumps(login_service.login({}))


if __name__ == "__main__":
    # Run the MCP server
    logger.info("Starting wolf 后端 MCP Server...")
    mcp.run(transport="streamable-http")
