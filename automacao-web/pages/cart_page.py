from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def ir_para_checkout(self):
        botao = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "checkout"))
        )
        self.driver.execute_script("arguments[0].click();", botao)
