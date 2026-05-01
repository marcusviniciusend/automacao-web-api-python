from selenium.webdriver.common.by import By


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    def adicionar_produto_ao_carrinho(self):
        # Localiza o botão de adicionar
        botao_adicionar = self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-backpack")
        # Força o clique via JavaScript para evitar que a Pipeline ignore a ação
        self.driver.execute_script("arguments[0].click();", botao_adicionar)

    def ir_para_carrinho(self):
        # Localiza o ícone do carrinho
        icone_carrinho = self.driver.find_element(
            By.CLASS_NAME, "shopping_cart_link")
        # Força o clique via JavaScript
        self.driver.execute_script("arguments[0].click();", icone_carrinho)
