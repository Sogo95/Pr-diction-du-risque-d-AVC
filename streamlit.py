
import streamlit as st
import pandas as pd
from joblib import load
from sklearn.preprocessing import LabelEncoder


# Chargement des données (Facultatif)
#df = pd.read_csv('data.csv', sep=';', decimal=',', encoding='ISO-8859-1')

# Chargement du modèle
model = load('modele.joblib')

# Titre de l'application
# Titre de l'application
st.title("Prédiction de risque d'avoir un AVC")
st.subheader('Auteur: SOGO Armel Emmanuel')
st.write("Selon l’Organisation Mondiale de la Santé (OMS) Chaque année, 15 millions de personnes font un accident vasculaire cérébral (AVC) : 5 millions d'entre elles meurent et 5 millions souffrent d'une incapacité permanente, ce qui représente un poids pour la famille et la communauté. La suspicion du diagnostic d'AVC repose en règle générale sur la clinique avec deux éléments clés à savoir un déficit neurologique focalisé et une apparition brutale. L'examen neurologique confirme le déficit, en précise la topographie et permet d'évoquer le territoire atteint. C’est dans le souci d’éviter les erreurs de diagnostiques, de réduire la charge du travail des cliniciens et de minimiser les coûts supportés par les patients que nous proposons un modèle de Machine Learning qui détectera le risque pour un patient donné d’avoir un AVC sur les patients positif en fonction de certaines caractéristiques. ")




def predict_AVC(sex1, age1, hypertension1, heart_disease1, ever_married1, work_type1, Residence_type1, avg_glucose_level1, bmi1, smoking_status1):
    
    # Définir un label encoder
    label_encoder_sexe = LabelEncoder()
    label_encoder_hypertension = LabelEncoder()
    label_encoder_heart_disease = LabelEncoder()
    label_encoder_ever_married = LabelEncoder()
    label_encoder_work_type= LabelEncoder()
    label_encoder_Residence_type = LabelEncoder()
    label_encoder_smoking_status = LabelEncoder()

    # Créer une liste de réponses possibles pour chaque question
    reponses_sexe = ['Masculin', 'Féminin']
    reponses_y_n = ['Oui', 'Non']
    reponses_residen= ['Urban', 'Rural']
    reponses_muti= ['Never_worked', 'children', 'Govt_job', 'Self-employed', 'Private']
    # Ajoutez les autres questions ici...

    # Adapter le label encoder à chaque liste de réponses
    label_encoder_sexe.fit(reponses_sexe)
    label_encoder_hypertension.fit(reponses_y_n)
    label_encoder_heart_disease.fit(reponses_y_n)
    label_encoder_ever_married.fit(reponses_y_n)
    label_encoder_smoking_status.fit(reponses_y_n)
    label_encoder_work_type.fit(reponses_muti)
    label_encoder_Residence_type.fit(reponses_residen)

    # Convertir les réponses en encodage numérique
    sex1 = label_encoder_sexe.transform([sex1])[0]
    hypertension1 = label_encoder_hypertension.transform([hypertension1])[0]
    heart_disease1 = label_encoder_heart_disease.transform([heart_disease1])[0]
    ever_married1 = label_encoder_ever_married.transform([ever_married1])[0]
    work_type1 = label_encoder_work_type.transform([work_type1])[0]
    Residence_type1 = label_encoder_Residence_type.transform([Residence_type1])[0]
    smoking_status1 = label_encoder_smoking_status.transform([smoking_status1])[0]

    
    
    # Encoder le sexe en utilisant l'encodeur de labels
    new_data = [[
        sex1,
        age1, 
        hypertension1, 
        heart_disease1, 
        ever_married1, 
        work_type1, 
        Residence_type1, 
        avg_glucose_level1, 
        bmi1, 
        smoking_status1
    ]]
    
    colonnes=['sex','age', 'hypertension', 'heart_disease', 'ever_married', 'work_type', 'Residence_type', 'avg_glucose_level', 'bmi', 'smoking_status']
    new_data = pd.DataFrame(new_data, columns=colonnes)

        
    # Faire la prédiction
    prediction = model.predict(new_data)
    
    return prediction


# Formulaire pour saisir les données d'entrée
sex1= st.radio('Sexe', ['Masculin', 'Féminin'])
age1=st.number_input('Quel est votre âge')
hypertension1= st.radio("Avez-vous déja eu de l'hypertension", ['Oui', 'Non'])
heart_disease1=st.radio("Avez-vous déja eu une maladie cardiaque ", ['Oui', 'Non'])
ever_married1=st.radio("Etes-vous marrié?", ['Oui', 'Non'])
work_type1=st.radio("Quel est votre type d'emploi?", ['Never_worked', 'children', 'Govt_job', 'Self-employed', 'Private'])
Residence_type1=st.radio("Quelle est votre zone de résidence?", ['Urban', 'Rural'])
avg_glucose_level1=st.number_input('Niveau de glycémie moyenne du patient')
bmi1 = st.number_input('Indice de masse corporelle')
smoking_status1=st.radio("Est-ce que le patient a déjà fumé?", ['Oui', 'Non'])


# Bouton pour effectuer la prédiction
if st.button('Prédire'):
    prediction =predict_AVC(sex1, age1, hypertension1, heart_disease1, ever_married1, work_type1, Residence_type1, avg_glucose_level1, bmi1, smoking_status1)
    st.success(f"Prédiction d'AVC: {prediction[0]}")