import pytest


@pytest.mark.asyncio
async def test_chat_creates_booking(client):
    response = await client.post(
        "/chat",
        headers={"Authorization": "Bearer super-secret-token"},
        json={
            "user_id": "test-user",
            "message": "book flight from sfo to jfk tomorrow",
        },
    )

    assert response.status_code == 200
    body = response.json()

    assert "Booked" in body["reply"]
    assert "CONF" in body["reply"]
