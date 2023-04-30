from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_all_posts():
    response = client.get('/posts/get')
    assert response.status_code == 200



def test_create_post():
    data = {"title": "Test Post", "content": "This is a test post."}
    response = client.post('/posts/create', json=data)
    assert response.status_code == 201


def test_update_post():
    data = {"title":"Updated", "content":"updated Content"}
    response = client.put('/posts/update/2', json=data)
    assert response.status_code==200

def tets_delete_post():
    response = client.delete('/posts/delete/2')
    assert response.status_code ==204 

