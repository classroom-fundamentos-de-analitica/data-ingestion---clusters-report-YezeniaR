"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd
import re

def ingest_data():

    with open('clusters_report.txt') as report:
        fila = report.readlines()

    clusters = []
    cluster = [0, 0, 0, '']
    fila = fila[4:]


    for i in fila:
        if re.match('^ +[0-9]+ +', i):
            numeroCluster, cantidadPalabras, porcentajePalabras, *ppalabras = i.split()
            cluster[0] = int(numeroCluster)
            cluster[1] = int(cantidadPalabras)
            cluster[2] = float(porcentajePalabras.replace(',','.')) 
            ppalabras.pop(0) 
            ppalabras = ' '.join(ppalabras)
            cluster[3] = cluster[3] + ppalabras

    
        elif re.match('^ +[a-z]', i):
            ppalabras = i.split()
            ppalabras = ' '.join(ppalabras)
            cluster[3] = cluster[3] + ' ' + ppalabras

        elif re.match('^\n', i) or re.match('^ +$', i):
            cluster[3] = cluster[3].replace('.', '')
            clusters.append(cluster)
            cluster = [0, 0, 0, '']

    df = pd.DataFrame (clusters, columns = ['cluster', 'cantidad_de_palabras_clave', 'porcentaje_de_palabras_clave', 'principales_palabras_clave'])
    return df
