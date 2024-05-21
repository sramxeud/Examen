import pandas as pd
import numpy as np

# Leer los datos del archivo CSV
datos = pd.read_csv('Automobile.csv')

# Seleccionar solo las columnas numéricas
datos_numericos = datos.select_dtypes(include=[np.number])

# Calcular el último cuartil y el percentil 80 para cada columna numérica
for columna in datos_numericos:
    ultimo_cuartil = datos_numericos[columna].quantile(0.75)
    percentil_80 = datos_numericos[columna].quantile(0.80)
    print(f"{columna}:")
    print(f"  Último cuartil: {ultimo_cuartil}")
    print(f"  Percentil 80: {percentil_80}")
