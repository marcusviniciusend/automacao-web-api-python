import time
import pytest
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

        login_page.abrir()
        login_page.fazer_login("standard_user", "secret_sauce")
        time.sleep(1) 
        assert "inventory" in driver.current_url

        inventory_page.adicionar_produto_ao_carrinho()
        inventory_page.ir_para_carrinho()
        time.sleep(1) 
        assert "cart" in driver.current_url

        cart_page.ir_para_checkout()
        time.sleep(1) 
        assert "checkout-step-one" in driver.current_url

        checkout_page.preencher_dados("Joao", "Silva", "12345")
        
        # Tava dando um problema com sincronismo aqui, essa pause resolveu, mas ideal seria usar WebDriverWait
        time.sleep(2) 
        assert "checkout-step-two" in driver.current_url

        checkout_page.finalizar_compra()
        assert checkout_page.obter_mensagem_confirmacao() == "Thank you for your order!"
