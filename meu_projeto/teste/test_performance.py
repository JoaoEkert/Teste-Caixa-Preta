import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager # type: ignore
from time import sleep

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

def teste_desempenho(driver):
    sleep(2)  # Espera 2 segundos antes de iniciar a medição de tempo

    start_time = time.time()
    driver.get("https://the-internet.herokuapp.com/login")
    load_time = time.time() - start_time

    print(f"Tempo de carregamento da página de login: {load_time} segundos")
