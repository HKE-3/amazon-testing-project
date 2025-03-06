import requests

BASE_URL = "https://petstore.swagger.io/v2"

# GET request - Tüm petleri getir
def test_get_pets():
    response = requests.get(f"{BASE_URL}/pet/findByStatus?status=available")
    assert response.status_code == 200
    print("GET Request Başarılı")

# POST request - Yeni bir pet ekle
def test_create_pet():
    new_pet = {"id": 12345, "name": "Test Pet", "status": "available"}
    response = requests.post(f"{BASE_URL}/pet", json=new_pet)
    assert response.status_code == 200
    print("POST Request Başarılı")

# PUT request - Pet bilgilerini güncelle
def test_update_pet():
    updated_pet = {"id": 12345, "name": "Updated Pet", "status": "sold"}
    response = requests.put(f"{BASE_URL}/pet", json=updated_pet)
    assert response.status_code == 200
    print("PUT Request Başarılı")

# DELETE request - Peti sil
def test_delete_pet():
    response = requests.delete(f"{BASE_URL}/pet/12345")
    assert response.status_code == 200
    print("DELETE Request Başarılı")

# Testleri çalıştır
if __name__ == "__main__":
    test_get_pets()
    test_create_pet()
    test_update_pet()
    test_delete_pet()
