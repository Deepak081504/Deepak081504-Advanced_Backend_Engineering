from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_home():

    response = client.get("/")

    assert response.status_code == 200


def test_register():

    response = client.post(
        "/auth/register",
        json={
            "name": "Deepak",
            "email": "deepak@gmail.com",
            "password": "123456",
            "role": "Admin"
        }
    )

    assert response.status_code == 200