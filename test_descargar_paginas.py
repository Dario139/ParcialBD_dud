from datetime import datetime
from urllib.request import urlopen
from bs4 import BeautifulSoup
import extraer_datos
import descargar_paginas

descargar_paginas.obtener_html()

csv_tiempo = extraer_datos.extraer()
    
def test_eltiempo():    
    assert csv_tiempo[0] == "En vivo movilidad de bogota nuevos cierres por caida de material en via al llano,Bogota,eltiempo.com/bogota/via-al-llano-movilidad-en-bogota-este-5-de-septiembre-802685"
