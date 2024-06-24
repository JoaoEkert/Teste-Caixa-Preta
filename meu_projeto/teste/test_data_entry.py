from selenium.webdriver.common.by import By
from time import sleep

def teste_entrada_dados(driver):
    driver.get("https://the-internet.herokuapp.com/login")
    sleep(2)  # Espera 2 segundos para a página carregar

    driver.find_element(By.ID, "username").send_keys("tomsmith")
    sleep(1)  # Espera 1 segundo antes de digitar a senha
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    sleep(1)  # Espera 1 segundo antes de imprimir a mensagem
    print("Entrada de dados bem-sucedida")
