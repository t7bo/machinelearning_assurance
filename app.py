import pickle
import streamlit as st 
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
from PIL import Image 
import base64
import io

import streamlit as st
data=pd.read_csv("clean_data.csv")
data = data.drop('bmi_categories',axis=1)


# Filtres horizontaux

menu= st.sidebar.radio("Menu", ["Charges prediction", "Analysis"])
if menu == "Analysis":
    st.title("Data analysis")
    st.image("assur.png", width=500)
    st.header("Sample of studied data")
    if st.checkbox("Data"):
        st.table(data.head(100))

    st.header("Descriptive analysis")
    if st.checkbox("Statistics"):
        st.table(data.describe())
    st.header("Correlations graphic")
    if st.checkbox("Correlations"):
        fig,ax=plt.subplots(figsize=(5,2.5))
        sns.heatmap(data.corr(numeric_only=True), cmap=sns.cubehelix_palette(as_cmap=True))
        st.pyplot(fig)



# Calcul de l'IMC
if menu == "Charges prediction":
    image = Image.open("assuraimant.png")

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
    # Utiliser la balise Markdown pour définir la taille du titre
    st.markdown("<h1 style=' font-size: 40px;'>Assur'aimant Insurance Cost Estimator</h1>", unsafe_allow_html=True)

    st.sidebar.header("Personal data")
    age = st.sidebar.slider("Age", 18, 100, 18)
    num_enfants = st.sidebar.number_input("Number of children", min_value=0, max_value=10, value=0)

    # Cases à cocher
    regions = st.sidebar.selectbox("Areas", ["northwest", "northeast", "southwest", "southeast"])
    genre = st.sidebar.selectbox("Gender", ["male", "female"])
    fumeur = st.sidebar.checkbox("Smoker")


    # Fumeurs
        
    if fumeur == True:
        smoker = "a smoker"
    else:
        smoker = "not a smoker"

    # Champs à remplir
    st.sidebar.header("Calculate your BMI")
    poids = st.sidebar.slider("Weight (kg)", 0, 300)
    taille = st.sidebar.slider("Height (m)", 0.0, 3.0)
    if poids > 0 and taille > 0:
        imc = poids / (taille ** 2)
        st.sidebar.write(f"BMI result : {imc:.2f}")
        st.header("Resume of your data")
        st.write(f"You are a **{genre}**, you are **{age}** years old and you have **{num_enfants}** child/children. You come from : **{regions}** and you are **{smoker}**. Your body mass index (BMI) is : **{imc:.2f}**")
        st.header(f"Charges' estimates you might pay if you choose our solution")
        st.write(f"With the data available, we can establish an approximate amount of charges you might pay with our solution. It would amount to : ")
        #st.markdown("<span style='color:green; font-size:54px;'>**4500 $**</span>", unsafe_allow_html=True)

        #dictionnaire = {"age" : age, "sex" : genre, "bmi" : imc, "children" : num_enfants, "smoker" : fumeur, "region" : region}
        dictionnaire = {"age" : [age], "sex" : [genre], "bmi" : [imc], "children" : [num_enfants], "smoker" : [fumeur], "region" : [regions]}
        df_a_predire = pd.DataFrame(dictionnaire)
        with open('modele.pkl', 'rb') as file:
            model = pickle.load(file)
            prediction = model.predict(df_a_predire)
            st.markdown(f"<span style='color:green; font-size:54px;'>**{round(prediction[0], 4)} $**</span>", unsafe_allow_html=True)



