from datetime import datetime
from descargar_paginas import get_url_tiempo, get_date, get_url_elespectador


def test_get_date():
    dt = get_date()
    assert dt == datetime.today().strftime('%Y-%m-%d')


def test_get_url_tiempo():
    assert get_url_tiempo() == "https://www.eltiempo.com/"


def test_get_url_elespectador():
    assert get_url_elespectador() == "https://www.elespectador.com/"
