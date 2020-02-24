from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.home.login_page import LoginPage
import unittest


class LoginTests(unittest.TestCase):

    def test_validLogin(self):
        baseURL = "https://learn.letskodeit.com/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)
        lp = LoginPage(driver)
        lp.login("nika.tukhashvili@yahoo.com","ZARNzarn123")

        driver.implicitly_wait(2)

        userIcon = driver.find_element(By.XPATH,'//li[@class="dropdown"]/a')
        if userIcon is not None:
            print("Login Successful")
        else:
            print("Login Not Succesful")

