

from modulos import modulos as md 
paht_1 = "./data/bicimad_stations.csv"
url ='https://datos.madrid.es/egob/catalogo/202162-0-instalaciones-accesibles-municip.json'
    
        
    # Damned Pipelines!
if __name__ == '__main__':
    
    
    DF_CSV = md.carga_datos_csv(paht_1)
    DF_CSV_CLEAN = md.procesar_coordenadas(DF_CSV)
    PULL_API =  md.datos_api(url)
    DF_API = md.crear_dataframe(PULL_API)
    DF_COMBINADO = md.calculo_de_distacias(DF_API,DF_CSV_CLEAN)
    DF_FINAL = md.distancias_min(DF_COMBINADO)
    nombre_archivo = input("  ingrese el nombre del archivo  ")
    LOAD = md.guardar_csv(DF_FINAL,nombre_archivo)