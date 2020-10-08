
from fastapi.testclient import TestClient

from app.server.app import app

client =  TestClient(app)

def test_read_main():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to this fantastic app!"}

def test_read_students_list():
    response = client.get('/students/')
    assert response.status_code == 200
    #assert response.json() == {"message": "Students data retrieved successfully"}