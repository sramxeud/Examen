from sklearn.preprocessing import MinMaxScaler
import pandas as pd
data = pd.read_csv('Automobile.csv')
min_max_scaler = MinMaxScaler()
data_minmax = min_max_scaler.fit_transform(
    data[['mpg', 'cylinders', 'displacement', 'weight', 'acceleration', 'model_year']])
print(data_minmax)
