#!/usr/bin/env python3
"""
wolf 后端 mcp
"""

import logging
from mcp.server.fastmcp import Context
from mcp.server.session import ServerSession
from server.server_context import ServerContext
from mcp.server.fastmcp import FastMCP
from mcp_session import McpSession

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def regist_mcp(mcp: FastMCP):
    """注册到mcp服务器"""

    @mcp.tool()
    async def login(ctx: Context[ServerSession, ServerContext]) -> dict:
        """登录到wolf系统

        Returns:
            包含登录用户信息，格式: {"userId": "用户ID", ...}
        """
        from service import login_service

        login_info = await login_service.login()
        session = McpSession.get_session(ctx.request_context.request)
        session["authrozition"] = login_info["authrozition"]
        return login_info["user_info"]

    @mcp.tool()
    async def ensure_segment_name_unique(name: str, ctx: Context) -> bool:
        """验证输入的分群名称是否已存在
        Args:
            name(str): 待验证的分群名称
        Returns(bool):
            分群名称是否重复
        """
        session = McpSession.get_session(ctx.request_context.request)
        authrozition = session["authrozition"]

        from service import segment_service

        is_unique = await segment_service.ensure_segment_name_unique(authrozition, name)
        return is_unique

    @mcp.tool()
    async def save_segment(name: str, ctx: Context) -> dict:
        """更新或者创建分群
        Args:
            name(str): 待创建的分群名称
        Returns:
            创建后的分群信息，格式如下
                {
                    "id": 2431, // 分群id
                    "name": "", // 分群名称
                    "status": "DRAFT" // 分群的状态
                }
        """
        session = McpSession.get_session(ctx.request_context.request)
        authrozition = session["authrozition"]

        from service import segment_service

        segment = await segment_service.save_segment(authrozition, name)
        return segment

    @mcp.tool()
    async def query_segment_list(
        name: str | None, ctx: Context[ServerSession, ServerContext]
    ) -> list:
        """查询分群的列表
        Args:
            name(str): 被查询的分群的名称。采用模糊查询。

        Returns:
            分群详细信息的列表，格式示例如下
                [{
                    "id": 2431, // 分群id
                    "name": "", // 分群名称
                    "createTime": 1712546717000, // 创建时间的时间戳
                    "status": "DRAFT" // 分群的状态
                }
            ]
        """
        from service import segment_service

        session = McpSession.get_session(ctx.request_context.request)
        authrozition = session["authrozition"]

        segments = await segment_service.query_segment_list(authrozition, name)
        return segments
