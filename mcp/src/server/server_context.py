from dataclasses import dataclass


@dataclass
class ServerContext:
    """
    app级别的上下文
    """

    data: str = "演示数据"
