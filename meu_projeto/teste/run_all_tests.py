import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from time import sleep, time
import HtmlTestRunner

class TestAuthentication(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def test_authentication(self):
        driver = self.driver
        start_time = time()  # Captura o tempo inicial
        
        driver.get("https://the-internet.herokuapp.com/login")
        
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
        except TimeoutException:
            self.fail("Timeout: Elemento 'username' não encontrado na página")
        
        # Agora o elemento "username" está presente na página
        driver.find_element(By.ID, "username").send_keys("tomsmith")
        sleep(1)  # Espera 1 segundo antes de digitar a senha
        
        driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
        sleep(1)  # Espera 1 segundo antes de clicar no botão
        
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        
        sleep(2)  # Espera 2 segundos para a autenticação processar
        
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".flash.success")))
            print("Autenticação bem-sucedida")
        except TimeoutException:
            self.fail("Falha na autenticação: Mensagem de sucesso não encontrada")
        
        end_time = time()  # Captura o tempo final
        elapsed_time = end_time - start_time
        print(f"Tempo total de execução: {elapsed_time:.2f} segundos")
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='test_reports'))
