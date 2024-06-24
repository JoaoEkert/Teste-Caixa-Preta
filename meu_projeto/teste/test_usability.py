from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

def teste_usabilidade(driver):
    driver.get("https://the-internet.herokuapp.com/login")
    sleep(2)  # Espera 2 segundos para a página carregar

    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
        print("Elemento de entrada de usuário encontrado, usabilidade ok")
    except:
        print("Elemento de entrada de usuário não encontrado, falha de usabilidade")
