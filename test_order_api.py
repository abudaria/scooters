import pytest
import requests
from config import API_URL
from data import order_payload

@pytest.fixture
def api_url():
    return API_URL

def test_get_order(api_url):
    create_order_url = f"{api_url}/api/v1/orders"
    get_order_url = f"{api_url}/v1/orders/track"

    response = requests.post(create_order_url, json=order_payload)

    order_data = response.json()
    track_number = order_data["track"]

    params = {
        "t": track_number
    }

    response = requests.get(get_order_url, params=params)
    assert response.status_code == 200, f"Ошибка при получении заказа по треку: {response.text}"
    print("Запрос на получение заказа по треку выполнен успешно.")
