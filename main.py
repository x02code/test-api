from requests import session
from logger import log
import time



session = session()
session.headers.update({'User-Agent': 'python-requests/2.25.1'})


def get_availble_pets():
    r = session.get(
        "https://petstore.swagger.io/v2/pet/findByStatus?status=available",
        timeout=(3, 10)
    )
    r.raise_for_status()
    return r.json()

def place_order(id :int):
    r = session.post(
    'https://petstore.swagger.io/v2/store/order',
        json={
            "id": id,
            "petId": 0,
            "quantity": 1,
            "shipDate": "2026-11-18T17:52:56.319Z",
            "status": "placed",
            "complete": True
        }
    )
    r.raise_for_status()
    return r.json()

if __name__ == "__main__":
    with session:
        try:
            avaliablePets = get_availble_pets()
            for i in avaliablePets:
                value = i.get("id")
                result = place_order(value)
                log(value, result)
                time.sleep(0.3)
        except Exception as e:
            print(e)