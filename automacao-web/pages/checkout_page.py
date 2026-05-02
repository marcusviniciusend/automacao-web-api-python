from selenium.webdriver.common.by import By


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def preencher_dados(self, nome, sobrenome, cep):
        self.driver.find_element(By.ID, "first-name").send_keys(nome)
        self.driver.find_element(By.ID, "last-name").send_keys(sobrenome)
        self.driver.find_element(By.ID, "postal-code").send_keys(cep)

        # Clique forçado via JavaScript para evitar que a Pipeline ignore a transição
        btn_continuar = self.driver.find_element(By.ID, "continue")
        self.driver.execute_script("arguments[0].click();", btn_continuar)

    def finalizar_compra(self):
        # Também vamos forçar o clique no Finish para não ter erro no último passo
        btn_finish = self.driver.find_element(By.ID, "finish")
        self.driver.execute_script("arguments[0].click();", btn_finish)

    def obter_mensagem_confirmacao(self):
        return self.driver.find_element(By.CLASS_NAME, "complete-header").text
