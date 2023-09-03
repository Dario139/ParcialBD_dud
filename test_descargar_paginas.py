from datetime import datetime
from extraer_datos import extraer


def test_eltiempo():
    eltiempo, elespectador = extraer()
    assert eltiempo[0] == "Durante 15 dias habra cierre en carriles del puente de la calle 127 con autonorte,Bogota,eltiempo.com/bogota/bogota-durante-15-dias-habra-cierre-en-carriles-del-puente-de-calle-127-con-autonorte-802268"

def test_get_url_tiempo():
    assert get_url_tiempo() == "https://www.eltiempo.com/"


def test_get_url_elespectador():
    assert get_url_elespectador() == "https://www.elespectador.com/"
