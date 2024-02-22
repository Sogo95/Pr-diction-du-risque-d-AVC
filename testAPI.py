from fastapi import FastAPI, HTTPException
import joblib, pickle
import numpy as np

app = FastAPI()

# Charger le modèle
model = joblib.load('modele.joblib')



@app.post('/predict')
async def predict(age: float, bmi: float, glucose: float):
    # Préparer les données pour la prédiction
    input_features = np.array([[age, bmi, glucose]])

    # Faire la prédiction
    prediction = model.predict(input_features)

    # Retourner la prédiction
    return {'prediction': prediction.tolist()}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='localhost', port=8000)



