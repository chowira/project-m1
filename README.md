
# Module 1 Project - Ironhack Part Time 🚀🚀

## Table of Contents
- [Project Structure](#project-structure)
- [Description](#description)
- [Requirements](#requirements)
- [Deployment](#deployment)
- [Conclusion](#conclusion)
- [Built With](#built-with)
- [References](#references)

## Project Structure 
```
│   .gitignore
│   main.py
│   README.md
│
├───.ipynb_checkpoints
├───basura
├───data
│       22
│       bicimad_stations.csv
│       bicipark_stations.csv
│       DF_COMBINADO
│       DF_COMBINADO.csv
│       prueba2
│       prueba_1.csv
│
├───desarrollo
│   │   dev_notebook_.ipynb
│   │
│   └───.ipynb_checkpoints
│           dev_notebook_-checkpoint.ipynb
│
└───modulos
    │   modulos.py
    │
    ├───.ipynb_checkpoints
    └───__pycache__
            modulos.cpython-310.pyc
            modulos.cpython-312.pyc
            modulos.cpython-39.pyc
```
## Description 📢 
This project aims to clean and process data from different formats to calculate the minimum distance between a point of interest and the nearest Bici Max station in Madrid.

## Requirements 📋 
Necessary libraries and dependencies:
- Python version == 3.10.14 
- geopandas == 1.0.1 
- requests == 2.32.3 

## Deployment 📦 
To run the `main.py` script, you must use the terminal and be located in the "proyecto de modulo uno" folder. Follow these steps:

1. **Execute the following code:**
    _python main.py --function "ALL"_ ⌨️
   This will result in a CSV file where you can specify the filename, containing a complete list of points of interest with the desired information.
   
    
   

2. **Execute the following code:**   
   _python main.py --function "LUGAR"_ ⌨️
   This allows you to perform a search by user input and returns only the row with the required information.

## Conclusion 📄 
If you follow the steps and use the necessary libraries and dependencies, you should not have any issues running it from the terminal.

## Built With 🛠️ 
- Jupyter Notebook 
- Python 

### Libraries  
- pandas 
- geopandas 
- requests 

## References 👨‍💻 
- [Pandas](https://pandas.pydata.org/) 
- [Geopandas](https://geopandas.org/en/stable/gallery/create_geopandas_from_pandas.html) 
- [Requests](https://requests.readthedocs.io/en/latest/) 