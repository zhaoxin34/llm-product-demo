import httpx

from service.base_service import BASE_URL, check_resp_rt_body


async def ajax_post(authrozition: str, url: str, json: dict | list):
    # 发送POST请求
    async with httpx.AsyncClient() as client:
        response = await client.post(
            url,
            json=json,
            headers={
                "Content-Type": "application/json",
                "Authorization": authrozition,
                "Project-Id": "qvAD1jk8q0hA0Oxm",
                "Dept-Ids": "678",
            },
        )
        response.raise_for_status()
        return check_resp_rt_body(response.json())


async def query_segment_list(authrozition: str, name: str | None) -> list:
    params = {
        "page": 1,
        "size": 10,
        "search": [],
        "sorts": [{"direction": "desc", "propertyName": "updateTime"}],
    }

    if name:
        params["search"].append(
            {
                "propertyName": "name",
                "operator": "LIKE",
                "value": name,
            },
        )

    # 构造请求URL
    url = f"{BASE_URL}/analyzer/analyzer/segment/query.do"

    body: dict = await ajax_post(authrozition, url, params)
    segments = []
    for segment in body["content"]:
        segments.append(
            {
                "id": segment["id"],
                "name": segment["name"],
                "status": segment["status"],
                "customerCount": segment["customerCount"],
                "createTime": segment["createTime"],
            }
        )

    return segments


async def ensure_segment_name_unique(authrozition: str, name: str) -> bool:
    params = {"name": name}
    url = f"{BASE_URL}/analyzer/analyzer/segment/ensureUnique.do"
    body: bool = await ajax_post(authrozition, url, params)
    return body


async def save_segment(authrozition: str, name: str) -> dict:
    """保存分群"""
    params = {
        "name": name,
        "validDateType": "FOREVER",
        "genre": "GENERAL",
        "scenario": {"id": 14},
        "whetherTest": False,
        "deptId": 678,
        "status": "DRAFT",
        "isDeleted": False,
        "type": "CONDITIONAL",
        "display": True,
        "step": 0,
    }
    # 构造请求URL
    url = f"{BASE_URL}/analyzer/analyzer/segment/save.do"
    body: dict = await ajax_post(authrozition, url, params)
    return {"id": body["id"], "name": body["name"]}
