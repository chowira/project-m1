# Proyecto del Módulo 1 - Ironhack Part Time

## Descripción
Este proyecto tiene como objetivo limpiar y operar datos provenientes de diferentes formatos para calcular la distancia mínima entre un punto de interés y la estación de Bici Max más cercana en Madrid.

## Problemática
A partir de unos datos contenidos en diferentes formatos, se busca obtener un conjunto de datos que devuelva la distancia mínima entre un punto de interés y la estación de Bici Max más cercana.

## Pasos a Seguir

### 1. Datos
#### 1.1 Bici Max
Los datos están contenidos en formato CSV en la carpeta `data`.

#### 1.2 Lugar de Interés
Los datos se obtienen a través de la API del [Portal de Datos Abiertos del Ayuntamiento de Madrid](https://datos.madrid.es/nuevoMadrid/swagger-ui-master-2.2.10/dist/index.html?url=/egobfiles/api.datos.madrid.es.json#/).

### 2. Desarrollo
Se exploran los datos y se definen los métodos a utilizar para resolver la problemática planteada. Se presenta una estrategia y se planifican las diferentes maneras de proceder, optando por la más conveniente.

#### 2.1 Funciones
Se crean funciones basadas en los pasos a seguir y en la exploración previa de los datos.

#### 2.2 Pruebas
Las funciones se prueban individualmente y en conjunto para asegurar su correcto funcionamiento.

### 3. Módulos
Una vez todo está funcionando, se crea el archivo `.py` llamado `modulos.py`, que contiene solo las funciones junto con sus librerías necesarias.

### 4. Script Principal
Se genera un archivo `main.py` donde se ejecuta la pipeline modificada para su uso específico.

### 5. Uso de Argparser
Se utiliza esta librería para ofrecer opciones al usuario al ejecutar el script mediante la función `argument_parser()`.

#### 5.1 Opción 1: "ALL"
Devuelve un CSV con todos los sitios de interés y la estación Bici Max más cercana, guardándolo en la carpeta `data`. Permite ingresar el nombre del archivo deseado.

#### 5.2 Opción 2: "LUGAR DE INTERÉS"
A partir del lugar de interés ingresado por el usuario, devuelve solo la fila correspondiente a dicho lugar.

## Conclusión
Este proyecto genera un programa que, al ejecutarlo con un CSV y datos desde la API del [Portal de Datos Abiertos del Ayuntamiento de Madrid](https://datos.madrid.es/nuevoMadrid/swagger-ui-master-2.2.10/dist/index.html?url=/egobfiles/api.datos.madrid.es.json#/), modifica y ejecuta operaciones necesarias para obtener resultados esperados, volviéndolos a cargar en un nuevo archivo CSV según la opción elegida por el usuario.

