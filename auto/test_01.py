from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


class TestWeb(unittest.TestCase):
    def test_one(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        browser.implicitly_wait(5)
        browser.find_element(By.CSS_SELECTOR, "body > div.container > form > div.first_block > div.form-group.first_class > input").send_keys("Vl")
        browser.find_element(By.XPATH, "/html/body/div[1]/form/div[1]/div[2]/input").send_keys("RG")
        browser.find_element(By.XPATH, "/html/body/div[1]/form/div[1]/div[3]/input").send_keys("@yandex")
        browser.find_element(By.CSS_SELECTOR,"body > div.container > form > div.second_block > div.form-group.first_class > input").send_keys("234")
        browser.find_element(By.XPATH, "/html/body/div[1]/form/div[2]/div[2]/input").send_keys("321")
        browser.find_element(By.CSS_SELECTOR, "body > div.container > form > button").click()
        message = browser.find_element(By.CSS_SELECTOR, "body > div.container > h1")
        message_text = message.text
        self.assertEqual(message_text, "Congratulations! You have successfully registered!", "Плохо всё")
    def test_two(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()

        browser.get(link)
        browser.implicitly_wait(5)
        browser.find_element(By.CSS_SELECTOR,
                             "body > div.container > form > div.first_block > div.form-group.first_class > input").send_keys(
            "123")
        browser.find_element(By.XPATH, "/html/body/div[1]/form/div[1]/div[2]/input").send_keys("321")
        browser.find_element(By.XPATH, "/html/body/div[1]/form/div[2]/div[1]/input").send_keys("333")
        browser.find_element(By.XPATH, "/html/body/div[1]/form/div[2]/div[2]/input").send_keys("444")
        browser.find_element(By.XPATH, "/html/body/div[1]/form/button").click()

        message = browser.find_element(By.CSS_SELECTOR, "body > div.container > h1")
        message_text = message.text
        self.assertEqual(message_text,"Congratulations! You have successfully registered!", "Всё плохо")

if __name__ == "__main__":
    unittest.main()




