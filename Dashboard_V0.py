# from operator import index
import sys, os

import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.pyplot import pie, axis, show
import plotly.express as px
from PIL import Image

cwd = os.getcwd()

st.set_page_config(layout="wide")

# Web Scrapping Dataframes
prix_dep = pd.read_csv(cwd+"/prix_dep.csv", index_col = 0)
prix_region = pd.read_csv(cwd+"/prix_region.csv", index_col = 0)
prix_ville = pd.read_csv(cwd+"/prix_ville.csv", index_col = 0)

# Analyse et Visualisation de données Dataframes
# RAW :
immo20 = pd.read_excel(cwd+'/immo.xlsx')
extrait20 = pd.read_csv(cwd+'/immo20_10.csv')
extrait21 = pd.read_csv(cwd+'/immo21_10.csv')
# Clean :
extrait20_clean = pd.read_csv(cwd+'/immo20_10clean.csv')
extrait21_clean = pd.read_csv(cwd+'/immo21_10clean.csv')
# Result :
extrait20_res = pd.read_csv(cwd+'/immo20_10res.csv')
extrait21_res = pd.read_csv(cwd+'/immo21_10res.csv')

@st.cache
def convert_df(df):
     # IMPORTANT: Cache the conversion to prevent computation on every rerun
     return df.to_csv().encode('utf-8')

csv_dep = convert_df(prix_dep)
csv_ville = convert_df(prix_ville)
csv_region = convert_df(prix_region)


def main():
    st.title("Storytelling: Prix et loyer immobiliers")
#     if st.button('Say hello'):
#           st.write('Why hello there')
#     else:
#           st.write('Goodbye')

    menu = ["Web Scraping", "Analyse et Netoyage De données", "Visualisation De données","Machine Learning"]
    choice = st.sidebar.selectbox("Menu",menu)

    if choice == 'Web Scraping':
            st.title('Web Scraping: TABLES')
            # st.write('')

            show = st.checkbox('Show Table Departements')
            if show:
                st.write("Table des depatements et leur prix et loyer par m2 :",prix_dep)
                st.download_button(
                        label="Download as CSV",
                        data=csv_dep,
                        file_name='prix_dep.csv',
                        mime='text/csv',
                  )
            show = st.checkbox('Show Table Cities')
            if show:
                st.write("Table des villes et leur prix et loyer par m2 :",prix_ville)
                st.download_button(
                        label="Download as CSV",
                        data=csv_dep,
                        file_name='prix_ville.csv',
                        mime='text/csv',
                  )

            show = st.checkbox('Show Table Regions')
            if show:
                st.write("Table des regions et leur prix et loyer par m2 :",prix_region)
                st.download_button(
                        label="Download as CSV",
                        data=csv_dep,
                        file_name='prix_region.csv',
                        mime='text/csv',
                  )

            st.write("[Map qui affiche le prix moyen des appartement par m2 dans les differents villes de l'Ile-De-France](https://datawrapper.dwcdn.net/Hdk9C/1/)")

    if choice == 'Analyse et Netoyage De données':
        st.title('Analyse et netoyage: \n Donnée 1:  Mutations de 2020')
        st.write('Extrait de la donnée RAW:', extrait20)
        col1, col2 = st.columns(2)

        with col1:
            st.text("")
            st.markdown("***")
            st.subheader("\n \n Notre data raw a 34169 rows × 45 columns, c'est une donnée des différents mutations éffectuées en 2020, ici vous voyez un extrait de 10 lignes.")
            st.write('\n')
            st.header("Colonnes de la donnée RAW:")
            st.image("img/columns2020.png")
        with col2:
            st.text("")
            st.markdown("***")
            st.header("Pourcentage des NaN :")
            def val_manq(df):
                ligne,colonne=df.shape
                nb_cell=ligne*colonne
                nb_null=df.isnull().sum().sum()
                prct=nb_null*100/nb_cell
                # st.write('Nombre de valeurs manquantes =',nb_null)
                # st.write('Nombre de cellulles totales =',nb_cell)
                st.write('Pourcentage de valeurs manquantes = ',round(prct,2),'%') 
                st.write('\n')
                st.write('Pourcentage de valeurs manquantes par variable/colonne =\n', round((df.isna().sum()*100/df.shape[0]),2).sort_values(ascending=True))
                st.write('\n')
                # plt.figure(figsize=(3,3))
                # # sns.heatmap(df.isna(), cbar=False)
                # fig, ax = plt.subplots()
                # sns.heatmap(df.isna(), cbar=False, ax=ax)
                # st.write(fig)
            val_manq(immo20)
            st.write()
        


        st.write('Extrait de la donnée après la suppression des colonnes vides:', extrait20_clean)
        col1, col2, col3 = st.columns(3)

        with col1:
            st.text("")
            st.markdown("***")
            st.subheader("\n \n Notre data clean a 34169 rows × 23 columns. Après la suppression de tous les colonnes vides, il nous reste cette donnée. Dans la 1ère illustration on voit la heatmap de notre donnée qui montre les valeurs égaux a NaN. \n Si la colonne est toute noire ca veut dire qu'il est toute remplie.")

        with col2:
            st.header("Corrélation de notre donnée avec Heatmap:")
            st.image('img/corr20.png')

        with col3:
            st.header("Colonnes de la donnée après netoyage:")
            st.image('img/coltypesclean20.png')
        
        st.write('Extrait de la donnée après tout le netoyage possible:', extrait20_res)
        
        st.title('Analyse et netoyage: \n Donnée 2:  Mutations de 2021')
        st.write('Extrait de la donnée RAW:', extrait21)
        
        col1, col2 = st.columns(2)

        with col1:
            st.text("")
            st.markdown("***")
            st.subheader("\n \n Notre data raw a 34169 rows × 45 columns, c'est une donnée des différents mutations affectuées en 2021, ici vous voyez un extrait de 10 lignes.")

        with col2:
            st.header("Colonne de la donnée RAW:")
            st.image('img/columns2021.png')


        st.write('Extrait de la donnée après la suppression des colonnes vides:', extrait21_clean)
        col1, col2 = st.columns(2)

        with col1:
            st.text("")
            st.markdown("***")
            st.subheader("\n \n Notre data clean a 34169 rows × 23 columns. Apres la suppression de tous les colonnes vides, il nous reste cette donnée. Dans la 1ere illustration on voit la heatmap de notre donnée qui montre les valeurs égaux a NaN. \n Si la colonne est toute noire ca veut dire qu'il est toute remplie.")

        with col2:
            st.header("Colonne de la donnée apres netoyage:")
            st.image('img/coltypesclean21.png')
        

        st.write('Extrait de la donnée après tout le netoyage possible:', extrait21_res)

    if choice == 'Visualisation De données':
            st.title('Visualisation de données: \n Donnée 1:  Mutations de 2020')
            # st.write('')
            
            col1, col2 = st.columns(2)

            with col1:
                st.text("")
                st.markdown("***")
                st.subheader("\n \n Ici vous voyez la boite a moustache qui montre la répartition des prix et les outlayers.")
                st.header("Boite a moustache des outlayers de la valeur fonciere:")
                st.image('img/moustache.png')

                st.text("")
                st.markdown("***")
                st.subheader("\n \n Pourcentage des apartements et des maisons par codepostal.")
                st.header("Pie part des types local:")
                st.image('img/ms_apt_pie.png')

                st.text("")
                st.markdown("***")
                st.subheader("\n \n Correlation de des mutations de l'année 2020.")
                st.header("Heatmap de la donnée 2020 netoyée:")
                st.image('img/corr_Df.png')

                st.text("")
                st.markdown("***")
                st.subheader("\n \n On voit ici les differents types de mutations éffectuées durant 2021, en addition du pourcentage de chaque type.")
                st.header("Piepart des types de mutations:")
                st.image('img/mutation_prc.png')

                
                st.text("")
                st.markdown("***")
                st.subheader("\n \n Cette illustartion montre la somme des surfaces reelles des batiments par departements..")
                st.header("Barplot la somme du surface par departement:")
                st.image('img/sum_dep_bar.png')

            with col2:
                st.text("")
                st.markdown("***")
                st.subheader("\n \n Cette corrélation nous montre la répartition des prix par IDCommune.")
                st.header("Correlation du repartition des prix:")
                st.image('img/roseprix.png')

                st.text("")
                st.markdown("***")
                st.subheader("\n \n Cee barplot decrit la moyenne des prix par mois de l'année 2020.")
                st.header("Barplot de la moyenne de valeur fonciere par mois:")
                st.image('img/moy_mois.png')


                st.text("")
                st.markdown("***")
                st.subheader("\n \n Correlation de des mutations de l'année 2021.")
                st.header("Heatmap de la donnée 2021 netoyée:")
                st.image('img/corr_df21.png')
                
                
                st.text("")
                st.markdown("***")
                st.subheader("\n \n Pour analyser la corrélation entre les variables dans notre jeu de données, nous utlisons la test spearman et pearson pour savoir la relation entre les variables quantitatives.")
                st.header("Spearman des variables des differents colonnes quantitatives pour l'année 2021:")
                st.image('img/spearman_df21.png')


                st.text("")
                st.markdown("***")
                st.subheader("\n \n Grâce à ce graphique, on voit que la valeur foncière est forte corrélé avec la departement du bien.")
                st.header("Barplot de la valeur fonciere par departement:")
                st.image('img/codedepcouleur.png')

    if choice ==  'Machine Learning':
            st.title("Machine learning : Prédiction des prix en utilisant les données de l'année 2020")
            # st.write('')

            alg = ["KNN", "Random forest"]
            alg_choisis = st.selectbox("Choisir Algorithme",alg)

            if alg_choisis == "KNN":
                st.write('Algorithme KNN : Predicting Valeure fonciere avec KNN Regression')
                st.header("Le score d'apres l'algorithme KNN Regression")

                col1, col2 = st.columns(2)
                with col1:
                    st.image('img/algoKNN.png')

                with col2:
                    st.image('img/KNN.png')
                

            if alg_choisis ==  "Decision Tree":
                st.write('Algorithme Random Forest: Predicting Valeure fonciere avec Random Forest')

                col1, col2 , col3= st.columns(3)

                with col1:
                    st.image('img/algoRF.png')

                with col2:
                    st.image('img/trainingdataRF.png')

                with col3:
                    st.image('img/testingdataRF.png')



            
                
                



if __name__ == '__main__':
    main()