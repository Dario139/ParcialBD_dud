import boto3
from datetime import datetime
from bs4 import BeautifulSoup


def funtionL():
    nombre = str(datetime.today().strftime('%Y-%m-%d'))
    s3 = boto3.resource('s3')
    bucket = s3.Bucket('parcialbigdatacorte1')
    obj_tiempo = bucket.Object(str("headlines/final/" +
                                   "eltiempo-" + nombre +
                                   ".html"))
    body_tiempo = obj_tiempo.get()['Body'].read()
    obj_elespectador = bucket.Object(str("headlines/final/" +
                                       "elespectador-" + nombre +
                                       ".html"))
    body_elespectador = obj_elespectador.get()['Body'].read()
  
    html_tiempo = BeautifulSoup(body_tiempo, 'html.parser')
    html_publimetro = BeautifulSoup(body_publimetro, 'html.parser')
  
    data_noticias_tiempo = html_tiempo.find_all('article')
    data_noticias_elespectador = html_elespectador.find_all('article')
    csv_tiempo = ""
    csv_elespectador = ""
    linea_0 = "Nombre, Categoria, Link\n"
    for i in range(len(data_noticias_tiempo)):
        link = "eltiempo.com" + \
               data_noticias_tiempo[i].find('a',
                                            class_='title page-link')['href']
        name = data_noticias_tiempo[i]['data-name'].replace(",", "")
        category = data_noticias_tiempo[i]['data-seccion']
        csv_tiempo += linea_0 + name + "," + \
            category + "," + \
            link + \
            "\n"
    for i in range(len(data_noticias_elespectador)):
        link = "elespectador.co" + data_noticias_elespectador[i].find('a')['href']
        name = (data_noticias_elespectador[i].find('a').text).replace(",", "")
        category = link.split('/')[1]
        csv_elespectador += linea_0 + name + "," + \
            category + "," + \
            link + \
            "\n"
    boto3.client('s3').put_object(Body=csv_tiempo,
                                  Bucket='parcialbigdatacorte1',
                                  Key=str('headlines/final' +
                                          '/periodico=eltiempo/year=' +
                                          nombre[:4]+'/month=' +
                                          nombre[5:7]+'/day=' +
                                          nombre[8:]+'/eltiempo.csv'))
    boto3.client('s3').put_object(Body=csv_elespectador,
                                  Bucket='parcialbigdatacorte1',
                                  Key=str('headlines/final' +
                                          '/periodico=elespectador/year=' +
                                          nombre[:4]+'/month=' +
                                          nombre[5:7]+'/day=' +
                                          nombre[8:]+'/elespectador.csv'))
                                          
                                          
funtionL()
