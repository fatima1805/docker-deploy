import unittest
from app import app

class TestApp(unittest.TestCase):
    
    def setUp(self):
        # Set up test client
        self.app = app.test_client()
    
    def test_homepage_returns_200(self):
        # Test that homepage responds with status 200
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_homepage_contains_hello(self):
        # Test that homepage contains "Hello"
        response = self.app.get('/')
        self.assertIn(b'Hello', response.data)

if __name__ == '__main__':
    unittest.main()
