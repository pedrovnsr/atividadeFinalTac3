# tests/test_api_unittest.py

import unittest
from app.api_client import update_post

class TestPutRequest(unittest.TestCase):

    def test_update_post(self):
        post_id = 1
        new_title = "Título Atualizado"
        new_body = "Conteúdo atualizado do post."

        response = update_post(post_id, title=new_title, body=new_body)

        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertEqual(data["title"], new_title)
        self.assertEqual(data["body"], new_body)

if __name__ == "__main__":
    unittest.main()
