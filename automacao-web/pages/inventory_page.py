from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    def adicionar_produto_ao_carrinho(self):
        botao = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "add-to-cart-sauce-labs-backpack"))
        )
        self.driver.execute_script("arguments[0].click();", botao)

    def ir_para_carrinho(self):
        icone = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_link"))
        )
        self.driver.execute_script("arguments[0].click();", icone)
