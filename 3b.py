from sklearn.preprocessing import StandardScaler
import pandas as pd
data = pd.read_csv('Automobile.csv')
scaler = StandardScaler()
data_scaled = scaler.fit_transform(
    data[['mpg', 'cylinders', 'displacement', 'weight', 'acceleration', 'model_year']])
print(data_scaled)
