from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    def adicionar_produto_ao_carrinho(self):
        botao_adicionar = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
        )
        botao_adicionar.click()

    def ir_para_carrinho(self):
        icone_carrinho = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
        )
        icone_carrinho.click()
