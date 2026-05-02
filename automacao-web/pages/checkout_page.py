from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def preencher_dados(self, nome, sobrenome, cep):
        wait = WebDriverWait(self.driver, 10)

        campo_nome = wait.until(EC.element_to_be_clickable((By.ID, "first-name")))
        campo_nome.click()
        campo_nome.send_keys(nome)

        campo_sobrenome = wait.until(EC.element_to_be_clickable((By.ID, "last-name")))
        campo_sobrenome.click()
        campo_sobrenome.send_keys(sobrenome)

        campo_cep = wait.until(EC.element_to_be_clickable((By.ID, "postal-code")))
        campo_cep.click()
        campo_cep.send_keys(cep)

        wait.until(EC.element_to_be_clickable((By.ID, "continue"))).click()

    def finalizar_compra(self):
        btn_finish = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "finish"))
        )
        self.driver.execute_script("arguments[0].click();", btn_finish)

    def obter_mensagem_confirmacao(self):
        elemento = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "complete-header"))
        )
        return elemento.text
