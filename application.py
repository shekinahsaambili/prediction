from flask import Flask, request, jsonify, render_template, redirect
import joblib

# Charger le modèle de régression linéaire entraîné
model = joblib.load('modele_regression.pkl')

app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    # Récupérer les données du formulaire
    prix = float(request.form['prix'])

    # Faire la prédiction avec le modèle
    quantite_eau_predite = model.predict([[prix]])

    # Retourner la prédiction au format JSON
    #return jsonify({'quantite_eau_predite': quantite_eau_predite[0]})
    return render_template('index.html', quantite_eau_predite=quantite_eau_predite[0])

if __name__ == '__main__':
    app.run(debug=True)