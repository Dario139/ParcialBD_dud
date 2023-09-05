import boto3
from datetime import datetime
from bs4 import BeautifulSoup

nombre = datetime.today().strftime('%Y-%m-%d')
s3 = boto3.resource('s3')
bucket_name = 'parcialbigdatacorte1'
linea_0 = "Nombre,Categoria,Link\n"
csv_tiempo = []


def extraer():
    obj_tiempo = s3.Object(bucket_name,
                           f"news/raw/eltiempo-{nombre}+".html")
    body_tiempo = obj_tiempo.get()['Body'].read()
    html_tiempo = BeautifulSoup(body_tiempo, 'html.parser')
    data_noticias_tiempo = html_tiempo.find_all('article')

    for article in data_noticias_tiempo:
        link = "eltiempo.com" + article.find('a',
                                             class_='title page-link')['href']
        name = article['data-name'].replace(",", "")
        category = article['data-seccion']
        csv_tiempo.append(f"{name},{category},{link}")

    return csv_tiempo


def escribir():
    s3_client = boto3.client('s3')
    csv_tiempo_content = linea_0 + '\n'.join(csv_tiempo)

    s3_client.put_object(
        Body=csv_tiempo_content,
        Bucket=bucket_name,
        Key=f'''headlines/final/periodico=eltiempo/year={nombre[:4]}/
                month={nombre[5:7]}/day={nombre[8:]}/eltiempo.csv'''
    )


extraer()
escribir()
