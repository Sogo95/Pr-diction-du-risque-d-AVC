import pandas as pd
from joblib import load
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import uvicorn


# Chargement des données (cette ligne peut être retirée)
df = pd.read_csv('stroke_data.csv')

# Chargement du modèle
modele = load('modele.joblib')

# Création d'une nouvelle instance FastAPI
app = FastAPI()

# Définission d'une classe pour les requêtes
class RequestBody(BaseModel):
    age: float
    bmi: float
    glucose: float
    
# Définition de l'endpoint de prédiction
@app.post("/predict")  
async def predict(data: RequestBody):

    # Préparation des données pour la prédiction
    new_data = [[
        data.age,
        data.bmi,
        data.glucose
       ]]

    colonnes=['age', 'bmi', 'glucose']
    new_data=pd.DataFrame(new_data,columns=colonnes)

    # Prédiction
    prediction = modele.predict(new_data)

    prediction = prediction.tolist()  
    return JSONResponse(content={"Prédiction de AVC": prediction})

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)