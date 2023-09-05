from datetime import datetime
from urllib.request import urlopen
from bs4 import BeautifulSoup

csv_tiempo = []

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
    
    assert csv_tiempo[0] == "En vivo movilidad de bogota nuevos cierres por caida de material en via al llano,Bogota,eltiempo.com/bogota/via-al-llano-movilidad-en-bogota-este-5-de-septiembre-802685"
