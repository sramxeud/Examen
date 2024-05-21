import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

# Leer los datos de Excel en un DataFrame de pandas
df = pd.read_excel('Automobile cinco.xlsx')

# Crear el árbol de decisión
X = df.drop('3er nivel', axis=1)
y = df['3er nivel']
arbol = DecisionTreeClassifier()
arbol.fit(X, y)

# Visualizar el árbol de decisión
plt.figure(figsize=(12, 8))
plot_tree(arbol, filled=True, feature_names=X.columns)
plt.show()
