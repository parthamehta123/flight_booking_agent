import pytest
import requests

"""
NOTE:
Requires the API server to be running:
    make run
or
    docker compose up
"""


@pytest.mark.e2e
def test_real_booking():
    res = requests.post(
        "http://localhost:8000/chat",
        headers={"Authorization": "Bearer super-secret-token"},
        json={"user_id": "test", "message": "book flight from sfo to jfk tomorrow"},
    )

    assert res.status_code == 200
