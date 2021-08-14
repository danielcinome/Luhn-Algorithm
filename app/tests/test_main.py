from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_validate_credit_card():
    response = client.post(
        '/validate/credit_card',
        json={
            "card_number": "6011269884123600"
    })
    assert response.status_code == 200
    assert response.json() == {
        "luhn_valid": True,
        "card_type": "Discover"
    }

def test_validate_credit_card_spaces():
    response = client.post(
        '/validate/credit_card',
        json={
            "card_number": "5394 9057 5052 0382"
    })
    assert response.status_code == 200
    assert response.json() == {
        "luhn_valid": True,
        "card_type": "MasterCard"
    }

def test_validate_bad_credit_card():
    response = client.post(
        '/validate/credit_card',
        json={
            "card_number": "539490"
    })
    assert response.status_code == 422
    assert response.json() == {
        "detail": "Tarjeta invalida"
    }
    

def test_validate_not_digit_credit_card():
    response = client.post(
        '/validate/credit_card',
        json={
            "card_number": "5394905750520382a"
    })
    assert response.status_code == 422
    assert response.json() == {
        "detail": "La tarjeta de credito ingresada no es un número"
    }
