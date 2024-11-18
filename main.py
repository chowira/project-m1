

from modulos import modulos as md 
import pandas as pd 
paht_1 = "./data/bicimad_stations.csv"
url ='https://datos.madrid.es/egob/catalogo/202162-0-instalaciones-accesibles-municip.json'
paht_2="./data/todas_las_distacias.csv"

        
    # Damned Pipelines!
if __name__ == '__main__':
     
        if md.argument_parser().function == "ALL":
            nombre_archivo = input("  ingrese el nombre del archivo  ")
            #DF_CSV = md.carga_datos_csv(paht_1)
            #DF_CSV_CLEAN = md.procesar_coordenadas(DF_CSV)
            #DF_CSV_CLEAN_BONUS = md.calculo_bicis_disponibles(DF_CSV_CLEAN)
            #PULL_API =  md.datos_api(url)
            #DF_API = md.crear_dataframe(PULL_API)                                                                                                                                                                                                                                                      
            #DF_COMBINADO = md.calculo_de_distacias(DF_API,DF_CSV_CLEAN_BONUS)
            DF_COMBINADO =  pd.read_csv(paht_2, sep= ",")
            DF_COMBINADO.columns = ["lugar de interes","distancia","address","street-address","bicis disponibles" ]
            print(DF_COMBINADO)
            DF_FINAL = md.distancias_min(DF_COMBINADO) 
            LOAD = md.guardar_csv(DF_FINAL,nombre_archivo)
        
        elif md.argument_parser().function == "LUGAR":
            #DF_CSV = md.carga_datos_csv(paht_1)
            #DF_CSV_CLEAN = md.procesar_coordenadas(DF_CSV)
            #DF_CSV_CLEAN_BONUS = md.calculo_bicis_disponibles(DF_CSV_CLEAN)
            #PULL_API =  md.datos_api(url)
            #DF_API = md.crear_dataframe(PULL_API)
            #DF_COMBINADO = md.calculo_de_distacias(DF_API,DF_CSV_CLEAN_BONUS)
            DF_COMBINADO =  pd.read_csv(paht_2, sep= ",")
            DF_COMBINADO.columns = ["lugar de interes","distancia","address","street-address","bicis disponibles" ]
            DF_FINAL = md.distancias_min(DF_COMBINADO)
            LUGAR_DE_INTERES = input(str("ingrese el lugar de interes :"))
            FILA = md.obtener_fila_por_lugar(DF_FINAL ,LUGAR_DE_INTERES)
            print(FILA)
            
        else:
            result = 'FATAL ERROR...you need to select the correct method'
            print(f'The result is => {result}') 

           
           
           #algunas direciones para probar 

            #Agencia de Proximidad de Arganzuela
            #Agente Tutor. Policía Municipal. Comisaría Integral de Distrito Vicálvaro
            #Aparcamiento para residentes. Antonio Mena
            #Aravaca Innovation Lab
            #Auditorio al aire libre. Parque Amós Acero