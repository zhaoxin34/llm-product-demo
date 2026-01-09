#!/usr/bin/env python3
"""
示例mcp，直接使用python deom.py即可启动
"""

import json
import logging
from datetime import datetime

from fastmcp import FastMCP

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create MCP server instance
mcp = FastMCP("DataAnalytics MCP", stateless_http=False, json_response=True)


@mcp.tool()
async def get_system_status() -> str:
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


if __name__ == "__main__":
    # Run the MCP server
    logger.info("Starting DataAnalytics MCP Server...")
    mcp.run(transport="streamable-http")

