from selenium.webdriver.common.by import By

URL = "https://www.saucedemo.com/"


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def abrir(self):
        self.driver.get(URL)

    def fazer_login(self, usuario, senha):
        self.driver.find_element(By.ID, "user-name").send_keys(usuario)
        self.driver.find_element(By.ID, "password").send_keys(senha)
        self.driver.find_element(By.ID, "login-button").click()
