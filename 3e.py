from sklearn.preprocessing import Binarizer
import pandas as pd
data = pd.read_csv('Automobile.csv')
binarizer = Binarizer(threshold=20)
mpg_binarized = binarizer.fit_transform(data[['mpg']])
print(mpg_binarized)
