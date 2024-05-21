
from sklearn.preprocessing import OneHotEncoder
import pandas as pd
datos = pd.read_csv('Automobile.csv')
encoder = OneHotEncoder()
origin_encoded = encoder.fit_transform(datos[['origin']])
print(origin_encoded)
