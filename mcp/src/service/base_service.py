# wolf系统API基础URL
BASE_URL = "http://wolf.dev.datatist.cn"


class WolfResponseException(Exception):
    """
    wolf响应的错误
    """
    def __init__(self, code: int, message: str):
        super().__init__(message)
        self.code = code
        self.message = message

    def __str__(self):
        return f"code：{self.code}; {self.message}"


def check_resp_rt_body(response: dict) -> dict:
    """
    检查response是否合法，并正确返回，如果返回是合法的，那么将body返回
    """
    header = response.get("header")
    if header is None:
        raise ValueError("'header' not in response")
    code = header.get("code")
    message = header.get("message")
    body = response.get("body")
    if code is None or code != 0:
        raise WolfResponseException(code, message)
    return body or {}

class WolfSession():
    """
    管理session
    """

    def __init__(self, userId: int, authorization: str):
        self.userId = userId
        self.authorization = authorization
