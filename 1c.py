import pandas as pd
import numpy as np
from scipy import stats

# Leemos los datos del archivo CSV
datos = pd.read_csv('Automobile.csv')

# Seleccionar solo las columnas numéricas
datos_numericos = datos.select_dtypes(include=[np.number])

# Calculo de la media, mediana, moda y media geométrica para cada columna numérica
for columna in datos_numericos:
    media = datos_numericos[columna].mean()
    mediana = datos_numericos[columna].median()
    moda = datos_numericos[columna].mode()[0]
    geometrica = stats.gmean(datos_numericos[columna])
    print(f"{columna}:")
    print(f"  Media: {media}")
    # Se ordenan los datos automáticamente antes de calcular la mediana
    print(f"  Mediana: {mediana}")
    print(f"  Moda: {moda}")
    print(f"  Media geométrica: {geometrica}")
