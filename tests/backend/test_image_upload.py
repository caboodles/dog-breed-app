import unittest
from backend.app import app

class TestImageUpload(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_upload(self):
        with open('test_image.jpg', 'rb') as img:
            response = self.app.post('/upload', data={'file': img})
            self.assertEqual(response.status_code, 200)
            data = response.get_json()
            self.assertIn('breed', data)

if __name__ == '__main__':
    unittest.main()
