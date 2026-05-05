from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

    def obter_mensagem_erro(self):
        elemento = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']"))
        )
        return elemento.text
