# usamos simpleImputer para los datos no numéricos
from sklearn.impute import SimpleImputer
import pandas as pd
import numpy as np

# Cargamos los datos
data = pd.read_csv('Automobile.csv')

# Creamos el imputer
imputer = SimpleImputer(strategy='mean')

# Seleccionamos sólo las columnas numéricas
data_numeric = data.select_dtypes(include=[np.number])

# Aplicamos el imputer a los datos numéricos
data_imputed = imputer.fit_transform(data_numeric)

print(data_imputed)
