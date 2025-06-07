import pytest
from app.service.tutor_service import ask_tutor

def test_ask_tutor():
    response = ask_tutor("O que são os Dessign Patterns?")
    print(response) 
    assert isinstance(response, str)
    assert len(response) > 0