from selenium.webdriver.common.by import By


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    def adicionar_produto_ao_carrinho(self):
        self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-backpack").click()

    def ir_para_carrinho(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
