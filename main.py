from requests import session
from logger import log
import time

TIMEOUT = (3, 10)

session = session()
session.headers.update({'User-Agent': 'python-requests/2.25.1'})


def get_availble_pets():
    r = session.get(
        "https://petstore.swagger.io/v2/pet/findByStatus?status=available",
        timeout = TIMEOUT
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
            "status": "placed",
            "complete": True
        },
        timeout = TIMEOUT
    )
    r.raise_for_status()
    return r.json()

if __name__ == "__main__":
    with session:
        try:
            avaliablePets = get_availble_pets()
        except Exception as e:
            print(e)
        else:
            for i in avaliablePets:
                value = i.get("id")
                try:
                    result = place_order(value)
                except Exception as e:
                    log(value, e)
                else:
                    log(value, result)
                time.sleep(0.3)