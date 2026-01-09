import httpx
import json
import base64

BASE_URL = "http://wolf.dev.datatist.cn"


async def login(user_info) -> dict:
    # 构造登录参数 (基于api-test.http中的示例)
    login_params = {
        "username": "15683100475",  # 用户名
        "password": "abcd1234",  # 密码
        "rememberMe": False,  # 记住我
        "scope": "AOOZJVR",  # 系统代码
    }

    # 将参数转换为JSON并base64编码
    json_params = json.dumps(login_params)
    encoded_params = base64.b64encode(json_params.encode()).decode()

    # 构造请求URL
    login_url = f"{BASE_URL}/analyzer/analyzer/account/autoTestLogin.do"
    return {"test": "abc"}

    # try:
    #     # 发送POST请求
    #     async with httpx.AsyncClient() as client:
    #         data = {"encryptLoginParams": encoded_params}
    #         async with client.post(
    #             login_url,
    #             data=data,
    #             headers={
    #                 "Accept-Language": "zh_CN",
    #                 "Content-Type": "application/x-www-form-urlencoded",
    #             },
    #         ) as response:
    #             # 检查响应状态
    #             if response.status == 200:
    #                 response_data = await response.json()
    #
    #                 # 检查登录是否成功
    #                 if response_data.get("success"):
    #                     # 返回用户信息摘要
    #                     user_info = response_data.get("data", {})
    #                     return json.dumps(
    #                         {
    #                             "success": True,
    #                             "username": user_info.get("username"),
    #                             "userId": user_info.get("userId"),
    #                             "realName": user_info.get("realName"),
    #                             "token": response.headers.get("Authorization"),
    #                             "message": "登录成功",
    #                         },
    #                         ensure_ascii=False,
    #                         indent=2,
    #                     )
    #                 else:
    #                     # 登录失败
    #                     error_msg = response_data.get("message", "登录失败")
    #                     return json.dumps(
    #                         {
    #                             "success": False,
    #                             "error": error_msg,
    #                             "message": f"登录失败: {error_msg}",
    #                         },
    #                         ensure_ascii=False,
    #                         indent=2,
    #                     )
    #             else:
    #                 # HTTP请求失败
    #                 error_text = await response.text()
    #                 return json.dumps(
    #                     {
    #                         "success": False,
    #                         "error": f"HTTP {response.status}",
    #                         "message": f"请求失败: {error_text}",
    #                     },
    #                     ensure_ascii=False,
    #                     indent=2,
    #                 )
    #
    # except aiohttp.ClientError as e:
    #     # 网络错误处理
    #     return json.dumps(
    #         {"success": False, "error": str(e), "message": f"网络请求错误: {str(e)}"},
    #         ensure_ascii=False,
    #         indent=2,
    #     )
    # except Exception as e:
    #     # 其他错误处理
    #     return json.dumps(
    #         {"success": False, "error": str(e), "message": f"系统错误: {str(e)}"},
    #         ensure_ascii=False,
    #         indent=2,
    #     )
