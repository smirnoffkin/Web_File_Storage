import pytest
from fastapi.testclient import TestClient


# Test /imports

@pytest.mark.parametrize("item_json", [
    ({
        "items": [
            {
                "type": "FOLDER",
                "id": "069cb8d7-bbdd-47d3-ad8f-82ef4c269df1",
                "parentId": None
            }
        ],
        "updateDate": "2022-02-01T12:00:00Z"
    }),
    ({
        "items": [
            {
                "type": "FOLDER",
                "id": "d515e43f-f3f6-4471-bb77-6b455017a2d2",
                "parentId": "069cb8d7-bbdd-47d3-ad8f-82ef4c269df1"
            },
            {
                "type": "FILE",
                "url": "/file/url1",
                "id": "863e1a7a-1304-42ae-943b-179184c077e3",
                "parentId": "d515e43f-f3f6-4471-bb77-6b455017a2d2",
                "size": 128
            },
            {
                "type": "FILE",
                "url": "/file/url2",
                "id": "b1d8fd7d-2ae3-47d5-b2f9-0f094af800d4",
                "parentId": "d515e43f-f3f6-4471-bb77-6b455017a2d2",
                "size": 256
            }
        ],
        "updateDate": "2022-02-02T12:00:00Z"
    }),
    ({
        "items": [
            {
                "type": "FOLDER",
                "id": "1cc0129a-2bfe-474c-9ee6-d435bf5fc8f2",
                "parentId": "069cb8d7-bbdd-47d3-ad8f-82ef4c269df1"
            },
            {
                "type": "FILE",
                "url": "/file/url3",
                "id": "98883e8f-0507-482f-bce2-2fb306cf6483",
                "parentId": "1cc0129a-2bfe-474c-9ee6-d435bf5fc8f2",
                "size": 512
            },
            {
                "type": "FILE",
                "url": "/file/url4",
                "id": "74b81fda-9cdc-4b63-8927-c978afed5cf4",
                "parentId": "1cc0129a-2bfe-474c-9ee6-d435bf5fc8f2",
                "size": 1024
            }
        ],
        "updateDate": "2022-02-03T12:00:00Z"
    }),
    ({
        "items": [
            {
                "type": "FILE",
                "url": "/file/url5",
                "id": "73bc3b36-02d1-4245-ab35-3106c9ee1c65",
                "parentId": "1cc0129a-2bfe-474c-9ee6-d435bf5fc8f2",
                "size": 64
            }
        ],
        "updateDate": "2022-02-03T15:00:00Z"
    })
])
def test_create_item(client: TestClient, item_json):
    request = client.post("/imports", json=item_json)
    assert request.status_code == 200
    assert request.json()['updateDate'] == item_json['updateDate']


# Test /nodes

def test_get_all_items(client: TestClient):
    response = client.get("/nodes/")
    assert response.status_code == 200


@pytest.mark.parametrize("item_id, expected_tree", [
    ("98883e8f-0507-482f-bce2-2fb306cf6483", {
        "type": "FILE",
        "url": "/file/url3",
        "id": "98883e8f-0507-482f-bce2-2fb306cf6483",
        "parentId": "1cc0129a-2bfe-474c-9ee6-d435bf5fc8f2",
        "size": 512,
        "date": "2022-02-03T12:00:00Z",
        "children": None,
    }),
    ("1cc0129a-2bfe-474c-9ee6-d435bf5fc8f2", {
        "type": "FOLDER",
        "id": "1cc0129a-2bfe-474c-9ee6-d435bf5fc8f2",
        "parentId": "069cb8d7-bbdd-47d3-ad8f-82ef4c269df1",
        "size": 1600,
        "url": None,
        "date": "2022-02-03T15:00:00Z",
        "children": [
            {
                "type": "FILE",
                "url": "/file/url3",
                "id": "98883e8f-0507-482f-bce2-2fb306cf6483",
                "parentId": "1cc0129a-2bfe-474c-9ee6-d435bf5fc8f2",
                "size": 512,
                "date": "2022-02-03T12:00:00Z",
                "children": None,
            },
            {
                "type": "FILE",
                "url": "/file/url4",
                "id": "74b81fda-9cdc-4b63-8927-c978afed5cf4",
                "parentId": "1cc0129a-2bfe-474c-9ee6-d435bf5fc8f2",
                "size": 1024,
                "date": "2022-02-03T12:00:00Z",
                "children": None
            },
            {
                "type": "FILE",
                "url": "/file/url5",
                "id": "73bc3b36-02d1-4245-ab35-3106c9ee1c65",
                "parentId": "1cc0129a-2bfe-474c-9ee6-d435bf5fc8f2",
                "size": 64,
                "date": "2022-02-03T15:00:00Z",
                "children": None
            }
        ]
    }),
    ("069cb8d7-bbdd-47d3-ad8f-82ef4c269df1", {
        "id": "069cb8d7-bbdd-47d3-ad8f-82ef4c269df1",
        "type": "FOLDER",
        "size": 1984,
        "parentId": None,
        "url": None,
        "date": "2022-02-03T15:00:00Z",
        "children": [
          {
            "id": "d515e43f-f3f6-4471-bb77-6b455017a2d2",
            "type": "FOLDER",
            "size": 384,
            "parentId": "069cb8d7-bbdd-47d3-ad8f-82ef4c269df1",
            "url": None,
            "date": "2022-02-02T12:00:00Z",
            "children": [
              {
                "id": "863e1a7a-1304-42ae-943b-179184c077e3",
                "type": "FILE",
                "size": 128,
                "parentId": "d515e43f-f3f6-4471-bb77-6b455017a2d2",
                "url": "/file/url1",
                "date": "2022-02-02T12:00:00Z",
                "children": None
              },
              {
                "id": "b1d8fd7d-2ae3-47d5-b2f9-0f094af800d4",
                "type": "FILE",
                "size": 256,
                "parentId": "d515e43f-f3f6-4471-bb77-6b455017a2d2",
                "url": "/file/url2",
                "date": "2022-02-02T12:00:00Z",
                "children": None
              }
            ]
          },
          {
            "id": "1cc0129a-2bfe-474c-9ee6-d435bf5fc8f2",
            "type": "FOLDER",
            "size": 1600,
            "parentId": "069cb8d7-bbdd-47d3-ad8f-82ef4c269df1",
            "url": None,
            "date": "2022-02-03T15:00:00Z",
            "children": [
              {
                "id": "98883e8f-0507-482f-bce2-2fb306cf6483",
                "type": "FILE",
                "size": 512,
                "parentId": "1cc0129a-2bfe-474c-9ee6-d435bf5fc8f2",
                "url": "/file/url3",
                "date": "2022-02-03T12:00:00Z",
                "children": None
              },
              {
                "id": "74b81fda-9cdc-4b63-8927-c978afed5cf4",
                "type": "FILE",
                "size": 1024,
                "parentId": "1cc0129a-2bfe-474c-9ee6-d435bf5fc8f2",
                "url": "/file/url4",
                "date": "2022-02-03T12:00:00Z",
                "children": None
              },
              {
                "id": "73bc3b36-02d1-4245-ab35-3106c9ee1c65",
                "type": "FILE",
                "size": 64,
                "parentId": "1cc0129a-2bfe-474c-9ee6-d435bf5fc8f2",
                "url": "/file/url5",
                "date": "2022-02-03T15:00:00Z",
                "children": None
              }
            ]
          }
        ]
    })
])
def test_get_item(client: TestClient, item_id: str, expected_tree: dict):
    response = client.get(f"/nodes/{item_id}")
    assert response.status_code == 200
    assert response.json() == expected_tree


@pytest.mark.parametrize("item_id", [
    ("000000000"),
    ("1234"),
    ("abracadabra")
])
def test_get_item_not_exist(client: TestClient, item_id: str):
    response = client.get(f"/nodes/{item_id}")
    assert response.status_code == 404


# Test /delete

@pytest.mark.parametrize("item_id", [
    ("b1d8fd7d-2ae3-47d5-b2f9-0f094af800d4"),
    ("d515e43f-f3f6-4471-bb77-6b455017a2d2"),
    ("069cb8d7-bbdd-47d3-ad8f-82ef4c269df1")
])
def test_delete_item(client: TestClient, item_id: str):
    response = client.delete(f"/delete/{item_id}")
    assert response.status_code == 200
    assert response.json()['id'] == item_id


@pytest.mark.parametrize("item_id", [
    ("000000000"),
    ("1234"),
    ("abracadabra")
])
def test_delete_item_not_exist(client: TestClient, item_id: str):
    response = client.delete(f"/delete/{item_id}")
    assert response.status_code == 404
