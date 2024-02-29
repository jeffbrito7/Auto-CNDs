from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

# Inicializa o WebDriver do Selenium (necessário ter o navegador Chrome e o chromedriver instalados)
driver = webdriver.Chrome()

try:
    # Abre a página
    driver.get("https://webas.sefaz.pi.gov.br/certidaonft-web/index.xhtml")

    # Clica no botão "-" para abrir menu
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".ui-layout-center ui-widget-content ui-corner-all pe-layout-pane-content ui-layout-pane ui-layout-pane-center"))).click()

    # Clica no botão "Certidão Negativa de Débitos com a Divida Ativa - CNDA"
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".ui-menuitem-text"))).click()

    # Clica no botão "Consultar Certidão"
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".ui-menuitem ui-widget ui-corner-all"))).click()

    # Solicita o CNPJ para buscar
    cnpj = input("Digite o CNPJ que deseja consultar: ")

    # Localiza o campo CNPJ e insere o CNPJ fornecido pelo usuário
    cnpj_input = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.ID, "formulario:cnpjInput")))
    cnpj_input.clear()
    cnpj_input.send_keys(cnpj)

    # Clica no botão "Consultar"
    WebDriverWait(driver, 0).until(EC.element_to_be_clickable((By.ID, "formulario:consultarButton"))).click()

    # Aguarda a geração da certidão e clica no botão para gerar em PDF
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".ui-button-icon-left.ui-icon.ui-c.fa.fa-file-text"))).click()

    # Aguarda um tempo para a geração do PDF
    time.sleep(10)

    # Define o caminho onde o PDF será salvo
    caminho = r"D:\Downloads\CERTIDOES"
    # Cria o diretório se ele não existir
    if not os.path.exists(caminho):
        os.makedirs(caminho)

    # Salva a página como um arquivo PDF
    driver.save_screenshot(os.path.join(caminho, "certidao.pdf"))

finally:
    # Fecha o navegador
    driver.quit()
