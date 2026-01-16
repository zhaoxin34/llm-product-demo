from pydantic import BaseModel, Field
from typing import TypeVar, Generic

# 定义一个类型变量 T
T = TypeVar("T")


class WolfResponse(BaseModel, Generic[T]):
    """wolf API 调用的返回"""

    success: bool = Field(description="API调用是否成功", default=True)
    message: str | None = Field(
        description="API调用如果返回错误，则message是错误信息，否则返回None",
        default=None,
    )
    body: T | None = Field(description="API调用返回的体", default=None)
