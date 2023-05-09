from fastapi.testclient import TestClient
from myapi import app
from fastapi import status

client = TestClient(app)


def test_find_all_users():
    response = client.get("/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()
    response.json()
    

def test_create_user():
    response = client.post("/", json={"name": "Poonguzhali", "email": "Poonguzhali@gmail.com", "password": "senthan@"})
    assert response.status_code == status.HTTP_200_OK
    response.json()
       

def test_find_all_users_new():
    response = client.get("/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()[0]["email"]=="Adhitiyakarikalan@gmail.com"

    

    """(Why i am used 0 here is the response returns a list of dictionaries, we use [0] to access the first dictionary in the list)"""

def test_update_user():
    response = client.get("/")
    assert response.status_code == status.HTTP_200_OK
    users = response.json()
   
    user_id = users[0]["id"]
    response = client.put(f"/{user_id}", json={"name": "Vandhiyathevan", "email": "Adhitiyakarikalan@gmail.com", "password": "Adhitiya123@"})

    updated_user = response.json()
    assert updated_user["name"] == "Vandhiyathevan"

    response = client.get(f"/{user_id}")
    user = response.json()
    assert user["name"] == "Vandhiyathevan"
   


    
    





 







