from datetime import datetime
from urllib.request import urlopen
from bs4 import BeautifulSoup

def get_url_tiempo():
    return "https://www.eltiempo.com/"

def get_html(url):
    with urlopen(url) as response:
        html = response.read()
    return html
    
def test_eltiempo():
    body_tiempo = get_html(get_url_tiempo())
    html_tiempo = BeautifulSoup(body_tiempo, 'html.parser')
    data_noticias_tiempo = html_tiempo.find_all('article')

    for article in data_noticias_tiempo:
     link = "eltiempo.com" + article.find('a',
                                           class_='title page-link')['href']
     name = article['data-name'].replace(",", "")
     category = article['data-seccion']
     csv_tiempo.append(f"{name},{category},{link}")
    
    assert csv_tiempo[0] == "Durante 15 dias habra cierre en carriles del puente de la calle 127 con autonorte,Bogota,eltiempo.com/bogota/bogota-durante-15-dias-habra-cierre-en-carriles-del-puente-de-calle-127-con-autonorte-802268"
