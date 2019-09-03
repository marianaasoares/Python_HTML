import requests
from bs4 import BeautifulSoup

#url = "https://www.gta.ufrj.br/grad/06_1/wap/"
url = "http://g1.globo.com/"
# Usando requests
html = requests.get(url).text
soup = BeautifulSoup(html)

for i in soup.html.find_all('a'):
    print(i.text)
