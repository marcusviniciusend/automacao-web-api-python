from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

_SET_REACT_VALUE = """
    var setter = Object.getOwnPropertyDescriptor(
        window.HTMLInputElement.prototype, 'value'
    ).set;
    setter.call(arguments[0], arguments[1]);
    arguments[0].dispatchEvent(new Event('input', { bubbles: true }));
    arguments[0].dispatchEvent(new Event('change', { bubbles: true }));
"""


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def _preencher_campo(self, element_id, value):
        elemento = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, element_id))
        )
        self.driver.execute_script(_SET_REACT_VALUE, elemento, value)

    def preencher_dados(self, nome, sobrenome, cep):
        self._preencher_campo("first-name", nome)
        self._preencher_campo("last-name", sobrenome)
        self._preencher_campo("postal-code", cep)

        btn = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "continue"))
        )
        self.driver.execute_script("arguments[0].click();", btn)

    def finalizar_compra(self):
        btn = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "finish"))
        )
        self.driver.execute_script("arguments[0].click();", btn)

    def obter_mensagem_confirmacao(self):
        elemento = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "complete-header"))
        )
        return elemento.text
