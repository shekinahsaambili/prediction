import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib
import matplotlib.pyplot as plt
import numpy as np

# Charger le jeu de données à partir du fichier CSV
data = pd.read_csv('data.csv')
#data = pd.read_csv('data.csv', encoding='latin1')
# Diviser les données en fonction et cible
y = data[['Quantite']]
X = data['Prix']

# Diviser les données en ensembles d'entraînement (40%) et de test (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, train_size=0.8, random_state=0)

# Transformer les Series en tableaux bidimensionnels
X_train = np.array(X_train).reshape(-1, 1)
y_train = np.array(y_train).reshape(-1, 1)

# Créer et entraîner le modèle de régression linéaire
model = LinearRegression()
model.fit(X_train, y_train)

# Créer et entraîner le modèle de régression linéaire
model = LinearRegression()
model.fit(X_train, y_train)

plt.scatter(X_train,y_train, color='red', label='donnees')
plt.plot(X_test,y_test, color="yellow", label='regression')
plt.xlabel('montant')
plt.ylabel('quantité d\'eau')
plt.legend()
plt.show()

# Enregistrer le modèle entraîné
#joblib.dump(model, 'modele_regression.pkl')