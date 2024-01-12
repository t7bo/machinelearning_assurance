import streamlit as st
import time, pickle
import pandas as pd
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image

import base64
import io


data=pd.read_csv("clean_data.csv")
df = data.drop('bmi_index',axis=1)


menu= st.sidebar.radio("Menu", ["Charges estimator", "Analysis"])


if menu == "Analysis":
    st.title("Data analysis")
    # st.image("assur.png", width=500)
    st.header("Sample of studied data")
    if st.checkbox("Data"):
        st.table(df.head(100))

    st.header("Descriptive analysis")
    if st.checkbox("Statistics"):
        st.table(df.describe())
    st.header("Correlations graphic")
    if st.checkbox("Correlations"):
        fig,ax=plt.subplots(figsize=(5,2.5))
        sns.heatmap(df.corr(numeric_only=True), cmap=sns.cubehelix_palette(as_cmap=True))
        st.pyplot(fig)





if menu == "Charges estimator":

    # Charger une image
    image = Image.open("logo_ml_blue-removebg-rogne.png")

    # Convertir l'image en base64
    buffered = io.BytesIO()
    image.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()

    # Utiliser du HTML personnalisé pour aligner horizontalement l'image et le texte
    html_code = f"""
        <div style="display: flex; flex-direction: row; align-items: center; justify-content: center">
            <img src="data:image/png;base64,{img_str}" style="width: 200px; height: auto;">
        </div>
    """

    # Afficher le HTML personnalisé
    st.markdown(html_code, unsafe_allow_html=True)

    # # Afficher le HTML personnalisé
    # st.markdown(html_code, unsafe_allow_html=True)


    # Titre du formulaire
    st.title("Estimateur de frais d'assurance chez Assur'Aimant")# Pour ajouter de l'espace
    st.markdown("**Réalisé par Tibo & Melo**")

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

        if imc > 0 and imc < 18.5:
            imc_categ = "underweight"
        elif imc > 18.5 and imc < 24.9:
            imc_categ = "normal"
        elif imc > 24.9 and imc < 29.9:
            imc_categ = "overweight"
        elif imc > 29.9 and imc < 34.9:
            imc_categ = "obesity class 1"
        elif imc > 34.9 and imc < 39.9:
            imc_categ = "obesity class 2"
        else:
            imc_categ = "obesity class 3"

        st.sidebar.write(f"Votre IMC est : {imc:.2f}")
        st.header("Récapitulatif de vos informations")
        st.write(f"Vous êtes un(e) **{genre}**, vous avez **{age}** ans et **{num_enfants}** enfants. Vous venez de la région **{region}** et vous êtes **{smoker}**. Votre indice de masse corporelle est de **{imc:.2f}**")
        st.header("Estimation des charges que vous pourriez payer chez nous")
        st.write(f"Avec les informations en notre possession, nous pouvons établir un **montant maximal approximatif** de charges que vous auriez à payer chez nous. Ce montant s'éléverait à : ")
        #st.markdown("<span style='color:green; font-size:54px;'>**4500 $**</span>", unsafe_allow_html=True)


        #dictionnaire = {"age" : age, "sex" : genre, "bmi" : imc, "children" : num_enfants, "smoker" : fumeur, "region" : region}
        dictionnaire = {"age" : [age], "sex" : [genre], "bmi_categories" : [imc_categ], "children" : [num_enfants], "smoker" : [fumeur], "region" : [region]}
        df_a_predire = pd.DataFrame(dictionnaire)
        with open('modele.pkl', 'rb') as file:
            model = pickle.load(file)
            prediction = model.predict(df_a_predire)
            st.markdown(f"<span style='color:green; font-size:54px;'>**{round(prediction[0], 4)} $**</span>", unsafe_allow_html=True)