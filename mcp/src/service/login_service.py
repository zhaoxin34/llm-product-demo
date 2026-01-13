import httpx
import json
import base64

from service.base_service import BASE_URL, check_resp_rt_body


async def login() -> dict:
    """调用登录方法"""
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

    # 发送POST请求
    async with httpx.AsyncClient() as client:
        response = await client.post(
            login_url,
            data={"encryptLoginParams": encoded_params},
            headers={"Content-Type": "application/x-www-form-urlencoded"},
        )
        response.raise_for_status()
        body = check_resp_rt_body(response.json())
        authrozition = response.headers["authorization"]
        return {"user_info": body, "authrozition": authrozition}


if __name__ == "__main__":

    async def main():
        body = await login()
        print(body)

    import asyncio

    asyncio.run(main())
