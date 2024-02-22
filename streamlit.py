import streamlit as st
import pandas as pd
from joblib import load

# Chargement des données (Facultatif)
#df = pd.read_csv('data.csv', sep=';', decimal=',', encoding='ISO-8859-1')

# Chargement du modèle
model = load('modele.joblib')

# Titre de l'application
# Titre de l'application
st.title('Prédiction des émissions de CO2 en France')
st.subheader('Auteur: Ismael YODA')
st.write("Cette application est destinée à éffectuer la prévision moyenne annuelle des émissions de CO2 des véhicules commercialisés en France. Elle prend en entrée les caractéristiques techniques du véhicule et sa consommation en carburant et elle renvoie en sortie la prédiction de sa moyenne d'émission annuelle de CO2.")


# Définir une fonction de prédiction
def predict_CO2(age1,bmi1, glucose1):
    new_data = [[
        age1,
        bmi1,
        glucose1
    ]]

    colonnes=['age', 'bmi', 'glucose']
    new_data = pd.DataFrame(new_data, columns=colonnes)

    prediction = model.predict(new_data)
    return prediction

# Formulaire pour saisir les données d'entrée
age1 = st.number_input('age')
bmi1 = st.number_input('Indice de masse corporelle')
glucose1 = st.number_input('Taux de  de glucose moyen')

# Bouton pour effectuer la prédiction
if st.button('Prédire'):
    prediction = predict_CO2(age1, bmi1, bmi1)
    st.success(f'Prédiction de CO2: {prediction[0]}')