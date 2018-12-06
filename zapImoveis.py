from selenium import webdriver   # Importa o webdriver
from selenium.webdriver.chrome.options import Options  # Options para utilizar o chrome driver em modo HeadLess(sem interface gráfica)
from bs4 import BeautifulSoup

# Configurando o chromeDriver para o modo Headless
options = Options()
options.headless = True
driver = webdriver.Chrome(chrome_options=options)
page = '1'
url = 'https://www.zapimoveis.com.br/aluguel/imoveis/#{"pagina":"'+page+'","paginaOrigem":"Home","formato":"Lista"}'

driver.get(url)  # Faz o request


html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
informacao = soup.select('article div')
#informacao = soup.find_all('article', class_='minificha')
print(informacao)

# Pesquisar
from collections import defaultdict
dict_master = defaultdict(dict)
