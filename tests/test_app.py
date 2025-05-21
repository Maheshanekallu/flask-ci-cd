import pytest
from app import app, items

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_crud_flow(client):
    # Ensure items list is empty at start
    items.clear()

    # Test GET index page
    rv = client.get("/")
    assert rv.status_code == 200
    assert b"CRUD Application" in rv.data

    # Test Add item
    rv = client.post("/add", data={"item": "TestItem1"}, follow_redirects=True)
    assert rv.status_code == 200
    assert b"TestItem1" in rv.data
    assert items == ["TestItem1"]

    # Test Update item
    rv = client.post("/update/0", data={"item": "UpdatedItem"}, follow_redirects=True)
    assert rv.status_code == 200
    assert b"UpdatedItem" in rv.data
    assert items == ["UpdatedItem"]

    # Test Delete item
    rv = client.post("/delete/0", follow_redirects=True)
    assert rv.status_code == 200
    assert b"UpdatedItem" not in rv.data
    assert items == []
