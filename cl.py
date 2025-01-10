import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
from datetime import date

class CalculatorTest(unittest.TestCase):

    def setUp(self):
        # ตั้งค่า WebDriver และเปิดเว็บไซต์
        s = Service('D:\\Chrome Driver\\chromedriver.exe')
        self.driver = webdriver.Chrome(service=s)
        self.driver.get("https://www.calculator.net/")
        self.driver.set_window_size(1072, 816)

    def test_calculator_and_age(self):
        driver = self.driver
        
        # ใช้งาน Basic Calculator
        # กดปุ่มตัวเลข 3, 0, 0 และปุ่ม +, ตามด้วย 2 และ =
        driver.find_element(By.XPATH, '//span[text()="5"]').click()
        driver.find_element(By.XPATH, '//span[text()="0"]').click()
        driver.find_element(By.XPATH, '//span[text()="0"]').click()
        driver.find_element(By.XPATH, '//span[text()="+"]').click()
        driver.find_element(By.XPATH, '//span[text()="5"]').click()
        driver.find_element(By.XPATH, '//span[text()="="]').click()

        # รอให้ผลการคำนวณแสดง
        time.sleep(2)

        # ตรวจสอบผลลัพธ์ที่แสดงใน Basic Calculator
        result = driver.find_element(By.ID, "sciOutPut").text.strip()
        self.assertEqual(result, "505", "Calculation result is incorrect.")

        # คลิกไปที่ Age Calculator
        driver.find_element(By.LINK_TEXT, "Age Calculator").click()

        # รอหน้า Age Calculator โหลด
        time.sleep(2)

        # ตั้งค่า Date of Birth เป็น "2 Aug 2004"
        dob_month = Select(driver.find_element(By.XPATH, '//*[@id="today_Month_ID"]'))
        dob_month.select_by_visible_text("Sep")

        dob_day = Select(driver.find_element(By.XPATH, '//*[@id="today_Day_ID"]'))
        dob_day.select_by_visible_text("10")

        # ลบค่า 2025 ที่อยู่ในฟิลด์ปี
        dob_year = driver.find_element(By.XPATH, '//*[@id="today_Year_ID"]')
        
        for _ in range(4):
            dob_year.send_keys(Keys.BACKSPACE)

        # พิมพ์ปี 2004
        dob_year.send_keys("2004")

        # รอปุ่มที่ต้องการให้คลิกให้พร้อมแล้วคลิก
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div[3]/form/table/tbody/tr[3]/td[2]/input'))
        )
        button.click()

        # รอให้ผลลัพธ์ของการคำนวณอายุแสดง
        time.sleep(2)

        # ตรวจสอบผลลัพธ์ของ Age Calculator
        result_age = driver.find_element(By.CLASS_NAME, "h2result").text
        print("Age Calculation Result:", result_age)

    def tearDown(self):
        # ปิดเบราว์เซอร์หลังการทดสอบ
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()