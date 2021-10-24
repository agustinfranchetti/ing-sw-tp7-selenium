import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestAgregarProductoCarrito():
  def setup_method(self, method):
    self.driver = webdriver.Safari()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_agregar_producto_carrito(self):
    # Test name: AgregarProductoCarrito
    # Step # | name | target | value

    # 1 | open | https://www.venex.com.ar/computadoras-y-servidores/pcs-de-escritorio/pc-intel-i7-8700-coffee-lake-8gb-1tb-wifi.html | 
    self.driver.get("https://www.venex.com.ar/computadoras-y-servidores/pcs-de-escritorio/pc-intel-i7-8700-coffee-lake-8gb-1tb-wifi.html")
    # 2 | click | css=.btn-block | 
    self.driver.find_element(By.CSS_SELECTOR, ".btn-block").click()
    # 3 | finds quantity box by html id, and gets its value
    cantidad = self.driver.find_element(By.ID, "quantityProduct_10079").get_attribute("value")
    
    print("EL VALUE ENCONTRADO ES", cantidad)

    #checkeo que haya una cantidad = 1 del producto en el carrito
    assert int(cantidad) == 1
