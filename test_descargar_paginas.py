from datetime import datetime
from extraer_datos


def test_eltiempo():
    eltiempo = extraer()
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

def test_get_url_tiempo():
    assert get_url_tiempo() == "https://www.eltiempo.com/"


def test_get_url_elespectador():
    assert get_url_elespectador() == "https://www.elespectador.com/"
