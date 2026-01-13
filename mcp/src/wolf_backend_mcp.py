#!/usr/bin/env python3
"""
wolf 后端 mcp
"""

from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from dataclasses import dataclass
import logging
from mcp.server.fastmcp import Context, FastMCP
from mcp.server.session import ServerSession

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@dataclass
class AppContext:
    """
    app级别的上下文

    """

    data: str = "演示数据"


@asynccontextmanager
async def app_lifespan(server: FastMCP) -> AsyncIterator[AppContext]:
    """Manage application lifecycle with type-safe context."""
    # 可通过ctx.request_context.lifespan_context 访问到
    data = "initial a new value"
    yield AppContext(data=data)


# Create MCP server instance
mcp = FastMCP(
    "wolf 后端 MCP", stateless_http=False, json_response=True, lifespan=app_lifespan
)


@mcp.tool()
async def login(ctx: Context[ServerSession, AppContext]) -> dict:
    """登录到wolf系统

    Returns:
        包含登录用户信息，格式: {"userId": "用户ID", ...}
    """
    from service import login_service

    print("-" * 20)
    print(ctx.request_context)
    help(ctx.request_context.session)
    print("-" * 20)

    login_info = await login_service.login()
    return login_info["user_info"]


@mcp.tool()
async def query_segment_list(
    name: str | None, ctx: Context[ServerSession, AppContext]
) -> dict:
    """查询分群的列表
    Args:
        name(str): 被查询的分群的名称。采用模糊查询。

    Returns:
        分群详细信息的列表，格式示例如下
            [{
                "createTime": 1712546717000, // 创建时间的时间戳
                "updateTime": 1715155732000,
                "createUserId": 2229,
                "updateUserId": 2,
                "createUserName": "admin",
                "updateUserName": "analyzer",
                "projectId": "qvAD1jk8q0hA0Oxm",
                "deptId": 678,
                "deptRoutes": "0,678",
                "id": 2431,
                "name": "45465656565656dddd", // 分群名称
                "customerCount": 0,
                "status": "DRAFT",
                "calcStatus": "NOTRUN",
                "type": "CONDITIONAL",
                "genre": "GENERAL",
                "defaultGenre": 0,
                "validDateType": "TEMPORARY",
                "validBeginTime": 1715155732000,
                "validEndTime": 1712764800000,
                "display": true,
                "whetherTest": false,
                "isDeleted": false,
                "approvalStatus": "NONE"
            }
        ]
    """
    from service import segment_service

    info = await segment_service.query_segment_list(name)
    return info


if __name__ == "__main__":
    # Run the MCP server
    logger.info("Starting wolf 后端 MCP Server...")
    mcp.run(transport="streamable-http")
