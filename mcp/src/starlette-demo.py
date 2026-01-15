from starlette.applications import Starlette
from starlette.middleware.sessions import SessionMiddleware
from starlette.responses import JSONResponse
from starlette.routing import Route
import uvicorn


# 操作 session 的视图函数
async def get_session(request):
    # 获取 session 中的 "counter" 值，如果没有则为 0
    counter = request.session.get("counter", 0)
    counter += 1
    # 将更新后的 counter 存回 session
    request.session["counter"] = counter
    return JSONResponse({"counter": counter})


# 创建 Starlette 应用
app = Starlette(
    debug=True,
    routes=[
        Route("/get-session", get_session),
    ],
)

# 添加 SessionMiddleware
app.add_middleware(SessionMiddleware, secret_key="your-secret-key")

# 运行应用
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
