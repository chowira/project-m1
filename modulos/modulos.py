#LIBRERIAS NECESARIAS .

import geopandas as gpd
from shapely.geometry import Point
import pandas as pd
import ast
import requests
import argparse
import os


#funciones para calcular la distancia entre dos puntos apartir de sus coordenadas
def to_mercator(lat, long):
    # transform latitude/longitude data in degrees to pseudo-mercator coordinates in metres
    c = gpd.GeoSeries([Point(lat, long)], crs=4326)
    c = c.to_crs(3857)
    return c

def distance_meters(lat_start, long_start, lat_finish, long_finish):
    # return the distance in metres between to latitude/longitude pair points in degrees 
    # (e.g.: Start Point -> 40.4400607 / -3.6425358 End Point -> 40.4234825 / -3.6292625)
    start = to_mercator(lat_start, long_start)
    finish = to_mercator(lat_finish, long_finish)
    return start.distance(finish)


#PASO 1
# FUNCION PARA HACER UN DATAFRAME DE UN ARCHIVO CSV
#Acepta : la uri de un csv como argumento 
#Devuelve: Un DataFrame
def carga_datos_csv(uri , separador="\t"): 
    """
    Carga un archivo CSV en un DataFrame de Pandas.
    Retorna:
    pd.DataFrame: Un DataFrame con los datos cargados.
    Si falla la ruta te devuelve un mensaje de error"""

    
    
    try:
        df = pd.read_csv(uri, sep=separador)
        return df
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")
        return None
    
    
    
   #PASO 2 limpiar y obtener el dataframe con los datos como los queremos apartir del csv
   #Acepta: Un DataFrame como argumento
   #Devuelve: Un dataFrame en el cual se a modificado la columna  'geometry.coordinates' y crea dos columnas con la informacion como la necesitamos 

def procesar_coordenadas(df_csv):
    """Verifica que la columna 'geometry.coordinates' exista en el DataFrame.
    Le entra como parámetro un DataFrame.
    Devuelve un DataFrame con las columnas 'longitud_bicimad' y 'latitud_bicimad'."""
    
    
    
    if "geometry.coordinates" not in df_csv.columns:
        raise ValueError("La columna 'geometry.coordinates' no existe en el DataFrame.")
    
    df_csv["geometry.coordinates"] = df_csv["geometry.coordinates"].apply(ast.literal_eval)
    df_csv["longitud_bicimad"] = df_csv["geometry.coordinates"].apply(lambda row: row[0])
    df_csv["latitud_bicimad"] = df_csv["geometry.coordinates"].apply(lambda row: row[1])
    
    return df_csv



#PASO 3 : obtener datos de la api en forma de un json 
# Acepta: Una url como argumento 
# Devuelve:UN json(DICCIONARIO)


def datos_api(url):
    """
    Envía una solicitud GET a la URL especificada y devuelve los datos JSON.
    Parámetros:
    : La URL desde la cual se deben recuperar los datos JSON.
    Retorno:
    dict: Los datos JSON como un diccionario de Python, o None en caso de error.
    """

    
    
    
    headers = {'Accept': 'application/json'}
    try:        
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()  
        else:
            print(f"Error al obtener los datos: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Ocurrió un error: {e}")
        return None


#PASO 4: funcion que a partir del  json obtiene los datos de las keys necesarias y,los renombra y devuelve un DataFrame 
#Acepta : Un diccionario 
#Devuelve: Un DataFRAME con las modificaciones necesarias 

def crear_dataframe(dato_api):
    """ revisa si el contendo es un diccionario y sitiene la clave ["@graph"]
    Parametro: acepta un diccionario  con una clave llamada ["@graph"]
    devuelve:un dataframe con los datos deseados 
    """
    
    
    if not isinstance(dato_api, dict) or "@graph" not in dato_api : 
        raise ValueError("El parámetro 'dato_api' debe ser un diccionario con la clave '@graph'.")
    
    tabla1 = pd.DataFrame(dato_api["@graph"])
    df_address = tabla1["address"].apply(pd.Series)
    df_location = tabla1["location"].apply(pd.Series)
    df_title = tabla1["title"].apply(pd.Series)  
    df_final = pd.concat([df_address, df_location, df_title], axis=1)
    df_final = df_final[["street-address", "latitude", "longitude", 0]]
    df_final = df_final.rename(columns={0: "lugar de interes"})
    df_final = df_final.iloc[:, [0, 1, 2, 4]]
    return df_final

    
#PASO 4 : Funcion que combina los dos DataFrame y calacula su distancia entre el punto de interes y la estaciones de bici max
#Acepta: Dos Data Frame como argumento     
#Devuelve: Un DataFrame con las distancias entre el punto de interes y la estaciones de bici max
    
    
def calculo_de_distacias(df_1,df_2):
    """"acepta:dos dataframe 
    combinas dos dataframe por una columnas creadas en comunn"
    devuelve: el dataframe combinado con la colunma distancia"""
    
    
    df_1["key"] = 1
    df_2["key"] = 1
    df_combinado = pd.merge(df_1,df_2)
    df_combinado["distancia"] = df_combinado[0:1000].apply(lambda x: distance_meters(x["latitude"], x["longitude"],x["latitud_bicimad"], x["longitud_bicimad"] ), axis=1)
    return df_combinado      




#PASO 5:Agrupa y ordena el DataFrame tomando como referencia la distacias minima   
#Acepta:Un DataFrame como argumento 
#Devuelve: Un DataFrame que solo muestra la imformacion requerida (distancia ntre punto interes y la estacion de bici max mas cercana )


def distancias_min(df):
    """" Funcion que agrupa teniendo encuenta lugar de interes y distacia min ,
    renombra las columnas y se trae solo las filas con la info necesaria
    y elimina as columnas que no son necesarias """
    
    
    
    resultado = df.groupby('lugar de interes').agg({'distancia': ['idxmin', 'min']}).reset_index()
    resultado.columns = ['lugar de interes', 'idxmin', 'distancia min']
    indices_minimos = resultado[('idxmin')].dropna().astype(int)
    resultado_final = df.loc[indices_minimos]
    resultado_final = pd.merge(resultado, resultado_final[['lugar de interes', 'address', 'street-address', 'bicis disponibles']],on='lugar de interes')
    resultado_final = resultado_final.rename(columns={'address': 'estacion bici max', 'street-address': 'direccion de lugar de interes'})
    resultado_final = resultado_final.drop(columns=['idxmin'])
    return  resultado_final



#PASO 6 : Guarda el DataFrame en un csv.txt en la carpeta data
#Acepta: Dos parametros el DataFrame y el nombre del archivo
#Devuelve : Un mensaje de guarddo con la ruta


def guardar_csv(dataframe, nombre_archivo):
    """Funcion que guarda el DataFrame en un archivo csv.txt en 
    la carpeta data con el nombre del arvivo que queremos"""
    
    
    
    
    ruta_archivo = os.path.join('./data', nombre_archivo)
    dataframe.to_csv(ruta_archivo, index=False)
    print(f"Archivo guardado en: {ruta_archivo}")





# Argument parser function

def argument_parser():
    parser = argparse.ArgumentParser(description = 'Application for arithmetic calculations' )
    help_message = "You have two options. Option 1: ALL te devuelve un csv con todos los lugares de interes . Option 2: LUGAR DE INTERES       te da el sitio especifico"  
    parser.add_argument('-f', '--function', help=help_message, type=str)
    args = parser.parse_args()
    return args



#FUNCION: filtra y devuelve la fila dependiendo del string que le pases 
#Acepta:Un DataFrame como argumento y un string como segundo argumento 
#Devuelve :Si no esta devuelve un error y si esta te devuelve la fila con la info 

def obtener_fila_por_lugar(df, lugar_de_interes):
    """Funcion que filtra a partir de un string y verifica si el string esta en el 
    DataFrame. y te devuelve una unica fila con su contenido"""
    
    fila = df.loc[df['lugar de interes'] == lugar_de_interes]
    
    if fila.empty:
        return f"No se encontró el lugar de interés: {lugar_de_interes}"
    
    return fila


#BONUS:
#FUNCION: calculo de bicis disponibles
#PARAMETROS: DataFrame 
# DEVUELVE: DataFrame (con la columna bicisdisponibles)

def calculo_bicis_disponibles(df):
    
    """Funcion que hace el calculo de las bicis disponibles  """
    if not isinstance(df, pd.DataFrame):
        
        raise ValueError("El argumento debe ser un DataFrame de pandas.")
    df["bicis disponibles"]= df["total_bases"] - df["free_bases"]
    return df


























    