# Ковалев Иван, 16-я когорта - Финальный проект (2 часть). Инженер по тестированию плюс.

import requests
import pytest
from config import URL, CREATE_ORDER, TRACK_ID
from data import payload

@pytest.fixture(scope="session")
def create_order():
    response = requests.post(URL + CREATE_ORDER, json=payload)
    return response.json()

def test_get_order_by_track(create_order):
    track_id = str(create_order["track"])
    response = requests.get(URL + TRACK_ID + track_id)
    assert response.status_code == 200
