# tests/test_api_pytest.py

import pytest
from app.api_client import get_posts, get_post, create_post, delete_post, requests_get_title
import time

#Test 1: Test do GET
def test_get_posts_status_and_content():
    response = get_posts()
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0


#Test 2: Test do POST
def test_create_post():
    title = "Post de Teste"
    body = "Este é um post criado durante o teste automatizado."
    user_id = 1
    response = create_post(title, body, user_id)

    assert response.status_code == 201
    data = response.json()
    assert data["title"] == title

#Test 3  do PUT feito em Unittest no arquivo test_api_unittest

#Test 4: Test do DELETE
def test_delete_post():
    response = delete_post(1)
    assert response.status_code in [200, 204]

#Test 5: Test de tempo de resposta
def test_response_time_get_posts():
    start = time.time()
    response = get_posts()
    end = time.time()
    duration = end - start

    assert response.status_code == 200
    assert duration < 2  # segundos

# Test 6: Captura título da pagina
def test_get_title():
    title = requests_get_title()
    assert "JSONPlaceholder" in title

# Teste 9: Testes com multiplos posts
@pytest.mark.parametrize("post_id", [1, 2, 3])
def test_multi_posts(post_id):
    res = get_post(post_id)
    assert res.status_code == 200

