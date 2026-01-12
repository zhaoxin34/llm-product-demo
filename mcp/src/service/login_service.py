import httpx
import json
import base64

BASE_URL = "http://wolf.dev.datatist.cn"


async def login() -> dict:
    # 构造登录参数 (基于api-test.http中的示例)
    login_params = {
        "username": "15683100475",  # 用户名
        "password": "abcd1234",  # 密码
        "rememberMe": False,  # 记住我
        "scope": "ANALYZER",  # 系统代码
    }

    # 将参数转换为JSON并base64编码
    json_params = json.dumps(login_params)
    encoded_params = base64.b64encode(json_params.encode()).decode()

    # 构造请求URL
    login_url = f"{BASE_URL}/analyzer/analyzer/account/autoTestLogin.do"
    return {"test": "abc"}

