from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

def teste_autenticacao(driver):
    driver.get("https://the-internet.herokuapp.com/login")
    sleep(2)  # Espera 2 segundos para a página carregar

    driver.find_element(By.ID, "username").send_keys("tomsmith")
    sleep(1)  # Espera 1 segundo antes de digitar a senha
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    sleep(1)  # Espera 1 segundo antes de clicar no botão
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    sleep(2)  # Espera 2 segundos para a autenticação processar

    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".flash.success")))
        print("Autenticação bem-sucedida")
    except:
        print("Falha na autenticação")
