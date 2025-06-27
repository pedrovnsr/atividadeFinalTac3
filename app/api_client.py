# app/api_client.py

import re
import requests

from app.logger import logger

BASE_URL = "https://jsonplaceholder.typicode.com"

def get_posts():
    """Retorna a lista de posts"""
    url = f"{BASE_URL}/posts"
    response = requests.get(url)
    logger.info(f"GET /posts - Status: {response.status_code}")
    return response

def create_post(title, body, user_id):
    """Cria um novo post"""
    url = f"{BASE_URL}/posts"
    payload = {
        "title": title,
        "body": body,
        "userId": user_id
    }
    response = requests.post(url, json=payload)
    logger.info(f"POST /posts - Status: {response.status_code} - Payload: {payload}")
    return response

def update_post(post_id, title=None, body=None, user_id=None):
    """Atualiza um post existente"""
    url = f"{BASE_URL}/posts/{post_id}"
    payload = {
        "title": title,
        "body": body,
        "userId": user_id
    }
    # Remove os campos que não foram passados (None)
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.put(url, json=payload)
    logger.info(f"PUT /posts/{post_id} - Status: {response.status_code} - Payload: {payload}")
    return response

def delete_post(post_id):
    """Exclui um post"""
    url = f"{BASE_URL}/posts/{post_id}"
    response = requests.delete(url)
    logger.info(f"DELETE /posts/{post_id} - Status: {response.status_code}")
    return response

def requests_get_title():
    resp = requests.get(BASE_URL)
    match = re.search("<title>(.*)</title>", resp.text)
    if match:
        return match.group(1)
    else:
        raise Exception("Não foi possível capturar o título da página")
