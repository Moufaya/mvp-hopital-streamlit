import streamlit as st
import pandas as pd
import os

st.title("🏥 MVP – Gestion Hospitalière")
st.write("Chargement des données patients")

# Nom du fichier CSV dans le repo
file_name = "patients_nettoyes(1).csv"

# Vérification de la présence du fichier
if os.path.exists(file_name):
    df = pd.read_csv(file_name)
    st.success("Données patients chargées avec succès ✅")
    st.dataframe(df.head())
else:
    st.error("Fichier patients introuvable dans le dépôt")
    st.stop()
