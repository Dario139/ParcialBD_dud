import boto3
from datetime import datetime
from urllib.request import urlopen


def get_url_tiempo():
    return "https://www.eltiempo.com/"


def get_url_elespectador():
    return "https://www.elespectador.com/"


def get_boto():
    return boto3.client('s3')


def get_date():
    return datetime.today().strftime('%Y-%m-%d')


def get_html(url):
    with urlopen(url) as response:
        html = response.read()
    return html


def obtener_html():
    fecha_actual = get_date()
    html_tiempo = get_html(get_url_tiempo())
    html_publimetro = get_html(get_url_elespectador())
    s3 = get_boto()
    s3.put_object(Body=html_tiempo,
                  Bucket='parcialbigdatacorte1',
                  Key="news/raw/eltiempo-"+str(fecha_actual)+".html")
    s3.put_object(Body=html_publimetro,
                  Bucket='parcialbigdatacorte1',
                  Key="news/raw/elespecatdor-"+str(fecha_actual)+".html")


obtener_html()
