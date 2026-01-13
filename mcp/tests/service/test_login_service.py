import pytest

from service import login_service


@pytest.mark.asyncio
async def test_login():
    result = await login_service.login()
    assert result is not None
