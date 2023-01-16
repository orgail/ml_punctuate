from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}
    

def test_recognition():
    response = client.post("/recognition/",
        json={"text": "My name is Clara and I live in Berkeley."}
    )
    assert response.status_code == 200
    assert response.json() == "[{'entity': 'B-PER', 'score': 0.9966202, 'index': 4, 'word': 'Clara', 'start': 11, 'end': 16}, {'entity': 'B-LOC', 'score': 0.9912492, 'index': 9, 'word': 'Berkeley', 'start': 31, 'end': 39}]"

