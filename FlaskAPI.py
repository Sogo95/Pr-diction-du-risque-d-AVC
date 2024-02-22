from flask import Flask, request, jsonify, render_template
import pickle, joblib
from pydantic import BaseModel
import uvicorn
from fastapi import FastAPI
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import numpy as np
from fastapi.responses import JSONResponse


app = FastAPI()

# Charger le modèle
#with open('modele.pkl', 'rb') as f:
    #model = pickle.load(f)
model = joblib.load('modele.pkl')



# Définir une route pour les prédictions
@app.route('/predict')
#, methods=['POST']
def predict():
#def predict():
    # Préparation des données pour la prédiction
    #new_data = [[
       # data.Sex,
       # data.age,
        #data.hypertension,
        #data.heart_disease,
        #data.smoking_status,
        #data.avg_glucose_level,
        #data.bmi
    #]]
    #colonnes=['sex', 'age', 'HTA', 'heart_disease', 'smoking_status', 'avg_glucose_level', 'bmi']
    #new_data=pd.DataFrame(new_data,columns=colonnes)
    
    data = request.get_json()
    # Extraire les valeurs des variables d'entrée
    age = float(data['age'])
    bmi = float(data['bmi'])
    glucose = float(data['glucose'])

    input_features = np.array([[age, bmi, glucose]]) 

    # Faire la prédiction
    prediction = model.predict(input_features)

    # Retourner la prédiction au format JSON
    return jsonify({'prediction': prediction})

@app.route('/send-form-data')
def send_form_data():
    # Récupérer les données de formulaire envoyées dans le corps de la requête
    age = float(request.form['age'])
    bmi = float(request.form['bmi'])
    glucose = float(request.form['glucose'])
    # Ajouter d'autres variables selon votre modèle

    # Préparer les données pour la prédiction
    input_features = np.array([[age, bmi, glucose]])  # Mettre toutes les variables dans un tableau numpy

    # Faire la prédiction
    prediction = model.predict(input_features)

    # Retourner la prédiction au format JSON
    return jsonify({'prediction': prediction})




    # Faire une prédiction
    #prediction = model.predict(new_data)
    
    # Renvoyer les résultats au format JSON
    #return jsonify({'prediction': prediction.tolist()})
    #return f"La prédiction est {prediction}"
    #prediction = prediction.tolist()  
    #return JSONResponse(content={"Prédiction de AVC": prediction})
    #return render_template('resultat.html', prediction=prediction)

if __name__ == '__main__':
    
    uvicorn.run(app, host="127.0.0.1", port=5000)



