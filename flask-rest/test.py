import unittest
import app
import requests
import json

class TestFlaskApiUsingRequests(unittest.TestCase):
    def test_hello_world(self):
        response = requests.get('http://localhost:5000/key/python')
        self.assertEquals(response.json(), "flask")


class TestFlaskApi(unittest.TestCase):
    def setUp(self):
        self.app = app.app.test_client()

    def test_get_api(self):
        response = self.app.get('/key/python')
        self.assertEqual(json.loads(response.get_data()), "flask")

if __name__ == "__main__":
    unittest.main()