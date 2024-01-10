import streamlit as st
import time, pickle
import pandas as pd
import numpy as np 

# Titre du formulaire
st.title("Estimateur de frais d'assurance chez Assur'Aimant")# Pour ajouter de l'espace
st.markdown("**Réalisé par Tibo et Mêlody**")

# Filtres horizontaux
st.sidebar.header("Personal information")
# age = st.sidebar.number_input("Âge", 18, 90, value=18)
age = st.sidebar.slider("Age", 18, 100, 18)
num_enfants = st.sidebar.number_input("Number of children", min_value=0, max_value=10, value=0)

# Cases à cocher
region = st.sidebar.selectbox("Regions", ["northeast", "northwest", "southeast", "southwest"])
genre = st.sidebar.selectbox("Sex", ["male", "female"])
fumeur = st.sidebar.checkbox("Smoker")

# Fumeurs PB
if fumeur == True:
    smoker = "fumeur/fumeuse"
else:
    smoker = "non-fumeur/fumeuse"

# Champs à remplir
st.sidebar.header("Calculate your BMI")
poids = st.sidebar.slider("Weight (kg)", 0, 300)
taille = st.sidebar.slider("Height (m)", 0.0, 3.0)

# Calcul de l'IMC
if poids > 0 and taille > 0:
    imc = poids / (taille ** 2)
    st.sidebar.write(f"Votre IMC est : {imc:.2f}")
    st.header("Récapitulatif de vos informations")
    st.write(f"Vous êtes un(e) **{genre}**, vous avez **{age}** ans et **{num_enfants}** enfants. Vous venez de la région **{region}** et vous êtes **{smoker}**. Votre indice de masse corporelle est de **{imc:.2f}**")
    st.header("Estimation des charges que vous pourriez payer chez nous")
    st.write(f"Avec les informations en notre possession, nous pouvons établir un **montant approximatif** de charges que vous auriez à payer chez nous. Ce montant s'éléverait à : ")
    #st.markdown("<span style='color:green; font-size:54px;'>**4500 $**</span>", unsafe_allow_html=True)

    #dictionnaire = {"age" : age, "sex" : genre, "bmi" : imc, "children" : num_enfants, "smoker" : fumeur, "region" : region}
    dictionnaire = {"age" : [age], "sex" : [genre], "bmi" : [imc], "children" : [num_enfants], "smoker" : [fumeur], "region" : [region]}
    df_a_predire = pd.DataFrame(dictionnaire)
    with open('modele.pkl', 'rb') as file:
        model = pickle.load(file)
        prediction = model.predict(df_a_predire)
        st.markdown(f"<span style='color:green; font-size:54px;'>**{round(prediction[0], 4)} $**</span>", unsafe_allow_html=True)