import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.driver import criar_driver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@pytest.fixture
def driver():
    driver = criar_driver()
    yield driver
    driver.quit()


class TestE2ECompra:
    def test_fluxo_completo_de_compra(self, driver):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)
        checkout_page = CheckoutPage(driver)

        # Aumentamos para 40 segundos. É tempo de sobra para qualquer conexão.
        wait = WebDriverWait(driver, 40)

        login_page.abrir()
        login_page.fazer_login("standard_user", "secret_sauce")
        wait.until(EC.url_contains("inventory"))

        inventory_page.adicionar_produto_ao_carrinho()
        inventory_page.ir_para_carrinho()

        wait.until(EC.url_contains("cart"))

        cart_page.ir_para_checkout()
        wait.until(EC.url_contains("checkout-step-one"))

        checkout_page.preencher_dados("Joao", "Silva", "12345")

        wait.until(EC.url_contains("checkout-step-two"))

        checkout_page.finalizar_compra()

        # Espera o elemento de sucesso aparecer fisicamente
        wait.until(EC.url_contains("checkout-complete"))
        assert checkout_page.obter_mensagem_confirmacao() == "Thank you for your order!"
