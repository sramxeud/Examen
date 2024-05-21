import pandas as pd
import matplotlib.pyplot as plt

# Leer los datos del archivo CSV
df = pd.read_csv('Automobile.csv')

# Crear un histograma para cada columna numérica
df.hist(bins=50, figsize=(20, 15))
plt.show()
