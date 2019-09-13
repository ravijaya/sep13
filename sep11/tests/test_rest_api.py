import unittest
import requests
from unittest.mock import MagicMock


class TestCaseUserAPI(unittest.TestCase):
    def test_get_all_users(self):
        response = requests.get('http://127.0.0.2:5000/users')
        self.assertEqual(response.status_code, 200)
        self.assertIn("admin@localhost", response.text)


class TestCaseTokenAuth(unittest.TestCase):
    def test_token_auth(self):

        class Response:
            status_code = 200
            text = "refresh_token"

        requests.post = MagicMock(return_value=Response())
        param = dict(username='test2', password='test2')
        response = requests.post('http://127.0.0.1:5000/login', json=param)
        self.assertEqual(response.status_code, 200)
        self.assertIn("refresh_token", response.text)


if __name__ == '__main__':
    unittest.main()
