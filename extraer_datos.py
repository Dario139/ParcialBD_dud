import boto3
from datetime import datetime
from bs4 import BeautifulSoup


def functionL():
    nombre = datetime.today().strftime('%Y-%m-%d')
    s3 = boto3.resource('s3')
    bucket_name = 'parcialbigdatacorte1'

    obj_tiempo = s3.Object(bucket_name,
                           f'headlines/final/eltiempo-{nombre}.html')
    body_tiempo = obj_tiempo.get()['Body'].read()
    obj_elespectador = s3.Object(bucket_name, f'headlines/final/elespectador-{nombre}.html')
    body_elespectador = obj_elespectador.get()['Body'].read()

    html_tiempo = BeautifulSoup(body_tiempo, 'html.parser')
    html_elespectador = BeautifulSoup(body_elespectador, 'html.parser')
    data_noticias_tiempo = html_tiempo.find_all('article')
    data_noticias_elespectador = html_elespectador.find_all('article')

    linea_0 = "Nombre,Categoria,Link\n"
    csv_tiempo = []
    csv_elespectador = []

    for article in data_noticias_tiempo:
        link = "eltiempo.com" + article.find('a', class_='title page-link')['href']
        name = article['data-name'].replace(",", "")
        category = article['data-seccion']
        csv_tiempo.append(f"{name},{category},{link}")

    for article in data_noticias_elespectador:
        link = "elespectador.co" + article.find('a')['href']
        name = article.find('a').text.replace(",", "")
        category = link.split('/')[1]
        csv_elespectador.append(f"{name},{category},{link}")

    s3_client = boto3.client('s3')
    csv_tiempo_content = linea_0 + '\n'.join(csv_tiempo)
    csv_elespectador_content = linea_0 + '\n'.join(csv_elespectador)

    s3_client.put_object(Body=csv_tiempo_content,
                         Bucket=bucket_name,
                         Key=f'headlines/final/periodico=eltiempo/year={nombre[:4]}/month={nombre[5:7]}/day={nombre[8:]}/eltiempo.csv')

    s3_client.put_object(Body=csv_elespectador_content,
                         Bucket=bucket_name,
                         Key=f'headlines/final/periodico=elespectador/year={nombre[:4]}/month={nombre[5:7]}/day={nombre[8:]}/elespectador.csv')


functionL()
