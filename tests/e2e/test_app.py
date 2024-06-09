import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestApp(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_upload_page(self):
        self.driver.get('http://localhost:5000/upload.html')
        file_input = self.driver.find_element(By.ID, 'fileInput')
        file_input.send_keys('/path/to/your/test_image.jpg')  # Update path
        upload_button = self.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        upload_button.click()
        breed_info = self.driver.find_element(By.ID, 'breedInfo')
        self.assertTrue(breed_info.text.startswith('Breed:'))

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
