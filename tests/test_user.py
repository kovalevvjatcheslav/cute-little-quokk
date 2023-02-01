import pytest


class TestUser:
    @pytest.mark.asyncio
    async def test_sign_up(self, client):
        response = await client.get("/")
        print(response.status_code)
        print(response.json())
