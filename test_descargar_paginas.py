from datetime import datetime
from urllib.request import urlopen
from bs4 import BeautifulSoup
import extraer_datos

csv_tiempo = extraer_datos.extraer()

def get_url_tiempo():
    return "https://www.eltiempo.com/"

def get_html(url):
    with urlopen(url) as response:
        html = response.read()
    return html
    
def test_eltiempo():    
    assert csv_tiempo[0] == "En vivo movilidad de bogota nuevos cierres por caida de material en via al llano,Bogota,eltiempo.com/bogota/via-al-llano-movilidad-en-bogota-este-5-de-septiembre-802685"
