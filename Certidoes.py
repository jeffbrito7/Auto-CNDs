from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

# Inicializa o WebDriver do Selenium (necessário ter o navegador Chrome e o chromedriver instalados)
driver = webdriver.Chrome()

try:
    # Solicita o CNPJ e as datas de início e fim do período para buscar
    cnpj = input("Digite o CNPJ que deseja buscar: ")
    data_inicio = input("Digite a data de início do período (YYYY-MM-DD): ")
    data_fim = input("Digite a data de fim do período (YYYY-MM-DD): ")

    # Abre a página
    driver.get("https://solucoes.receita.fazenda.gov.br/Servicos/certidaointernet/PJ/Consultar")

    # Localiza os campos CNPJ, Data início e Data fim pelo ID usando a classe By
    cnpj_input = driver.find_element(By.ID, "Ni")
    data_inicio_input = driver.find_element(By.ID, "PeriodoInicio")
    data_fim_input = driver.find_element(By.ID, "PeriodoFim")

    # Insere o CNPJ e as datas fornecidas pelo usuário nos campos correspondentes
    cnpj_input.send_keys(cnpj)
    data_inicio_input.send_keys(data_inicio)
    data_fim_input.send_keys(data_fim)

    # Espera até que o botão "Consultar" seja visível
    consultar_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "validar"))
    )

    # Clica no botão "Consultar"
    consultar_button.click()

    # Aguarda um tempo para que a página carregue completamente
    time.sleep(30)  # Pode ser necessário ajustar esse tempo dependendo da velocidade do site

    # Define o caminho onde o screenshot será salvo
    caminho = r"D:\Downloads\CERTIDOES"
    # Cria o diretório se ele não existir
    if not os.path.exists(caminho):
        os.makedirs(caminho)

    # Salva o screenshot da página como um arquivo PNG
    driver.save_screenshot(os.path.join(caminho, "screenshot.png"))

finally:
    # Fecha o navegador
    driver.quit()
