import httpx

from service.base_service import BASE_URL, check_resp_rt_body


async def query_segment_list(name: str | None) -> dict:
    params = {
        "size": 10,
        "page": 1,
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

    # 发送POST请求
    async with httpx.AsyncClient() as client:
        response = await client.post(
            url,
            data=params,
            headers={"Content-Type": "application/json"},
        )
        response.raise_for_status()
        body = check_resp_rt_body(response.json())
        return body["content"]
