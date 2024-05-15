from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_optimize():
    payload = {
        "capacity": 1000,
        "points": [
            {"id": 10844090706, "lat": 60.023117, "long": 30.326293, "type": "outpost",
             "adress": "112 к1, проспект Тореза, Поклонная гора, округ Светлановское, Санкт-Петербург, Северо-Западный федеральный округ, 194017, Россия",
             "total_volume": 376, "free_volume": 211, "purpose": "Ozon"},
            {"id": 10672598289, "lat": 60.0002165, "long": 30.2537662, "type": "outpost",
             "adress": "20 к1, Гаккелевская улица, округ № 65, Санкт-Петербург, Северо-Западный федеральный округ, 197372, Россия",
             "total_volume": 438, "free_volume": 275, "purpose": "Яндекс.Маркет"},
            {"id": 6308159165, "lat": 59.9555962, "long": 30.2469113, "type": "",
             "adress": "Пункт самовывоза, Уральская улица, округ Остров Декабристов, Санкт-Петербург, Северо-Западный федеральный округ, 199155, Россия",
             "total_volume": 0, "free_volume": 0, "purpose": ""},
            {"id": 10763697408, "lat": 59.9655866, "long": 30.2884309, "type": "outpost",
             "adress": "Ozon, 13, Петрозаводская улица, Петроградская сторона, округ Чкаловское, Санкт-Петербург, Северо-Западный федеральный округ, 197198, Россия",
             "total_volume": 276, "free_volume": 203, "purpose": "Ozon"},
            {"id": 11169616069, "lat": 59.9616437, "long": 30.3302693, "type": "outpost",
             "adress": "Ozon, 3/12, улица Котовского, Петроградская сторона, Посадский округ, Санкт-Петербург, Северо-Западный федеральный округ, 197101, Россия",
             "total_volume": 398, "free_volume": 236, "purpose": "Ozon"},
            {"id": 11304463470, "lat": 59.919949, "long": 30.3618819, "type": "outpost",
             "adress": "Ozon, 11, Транспортный переулок, округ Лиговка-Ямская, Санкт-Петербург, Северо-Западный федеральный округ, 190961, Россия",
             "total_volume": 478, "free_volume": 275, "purpose": "Ozon"},
            {"id": 2216518883, "lat": 59.9117302, "long": 30.3215055, "type": "outpost",
             "adress": "34, Малодетскосельский проспект, округ Семёновский, Санкт-Петербург, Северо-Западный федеральный округ, 190013, Россия",
             "total_volume": 538, "free_volume": 355, "purpose": "Ozon"},
            {"id": 10844090935, "lat": 59.849079, "long": 30.323002, "type": "outpost",
             "adress": "216, Московский проспект, Средняя Рогатка, округ Звёздное, Санкт-Петербург, Северо-Западный федеральный округ, 196066, Россия",
             "total_volume": 418, "free_volume": 254, "purpose": "Ozon"},
            {"id": 11169616022, "lat": 59.8601635, "long": 30.3573677, "type": "outpost",
             "adress": "Ozon, 31 к2, Витебский проспект, округ Гагаринское, Санкт-Петербург, Северо-Западный федеральный округ, 196244, Россия",
             "total_volume": 297, "free_volume": 210, "purpose": "Ozon"},
            {"id": 9076608902, "lat": 59.8441991, "long": 30.4086864, "type": "outpost",
             "adress": "Ozon, 124/56, Бухарестская улица, Александровский округ, Санкт-Петербург, Северо-Западный федеральный округ, 192284, Россия",
             "total_volume": 439, "free_volume": 269, "purpose": "Ozon"}
        ]}
    response = client.post("/optimize", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "_id" in data
    assert "route" in data


def test_get_route_by_id():
    response = client.get("/route?id=663662ca9494b67cea8c85de")
    assert response.status_code == 200
    data = response.json()
    assert data["_id"] == "663662ca9494b67cea8c85de"
    assert len(data["route"]) > 0


def test_get_route_by_amount():
    response = client.get("/route?amount=10")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 10
