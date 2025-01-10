import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ClickBox(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument('--disable-gpu')
        self.service = Service('D:\\Chrome Driver\\chromedriver.exe')
        self.driver = webdriver.Chrome(service=self.service, options=options)
        self.driver.get("https://lemon-meadow-0c732f100.5.azurestaticapps.net/")  # Fixed URL
        self.driver.set_window_size(1072, 816)

    def tearDown(self):
        self.driver.quit()  # Properly close the browser session

    def test_CheckAndTickBox(self):

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, '0'))
        )

        script = """
        var unchecked = [];
        for (var i = 0; i < 100; i++) {
            var checkbox = document.getElementById(i);
            if (checkbox && checkbox.type === 'checkbox') {
                if (!checkbox.checked) { // ถ้ายังไม่ได้ติ๊ก
                    unchecked.push(i);  // เก็บ id ของ checkbox ที่ไม่ได้ติ๊ก
                    checkbox.click();   // ติ๊ก checkbox อัตโนมัติ
                }
            }
        }
        return unchecked; // คืนค่า id ของ checkbox ที่ถูกติ๊ก
        """
        unchecked_boxes = self.driver.execute_script(script)
        print("Checkboxes that were unchecked and now clicked:", unchecked_boxes)

        time.sleep(5)  # Adjusted sleep time

if __name__ == "__main__":
    unittest.main()
