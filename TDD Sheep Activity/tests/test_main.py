import sys
import os

from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_read_sheep():

    response = client.get("/sheep/1")

    assert response.status_code == 200

    assert response.json() == {

        "id": 1,
        "name": "Spice",
        "breed": "Gotland",
        "sex": "ewe"
    }


def test_add_sheep():
    new_sheep = {
        "id": 7,
        "name": "Larry",
        "breed": "Suffolk",
        "sex": "ewe"
    }

    response = client.post("/sheep", json=new_sheep)

    assert response.status_code == 201

    response_data = response.json()

    assert response_data["name"] == new_sheep["name"]
    assert response_data["breed"] == new_sheep["breed"]
    assert response_data["sex"] == new_sheep["sex"]

    assert "id" in response_data

    sheep_id = response_data["id"]

    get_response = client.get(f"/sheep/{sheep_id}")

    assert get_response.status_code == 200

    retrieved_sheep = get_response.json()

    assert retrieved_sheep == response_data

