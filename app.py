# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 21:37:51 2024

@author: Hp
"""
import streamlit as st
import pandas as pd
import pickle as pkl

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
    recommended_movie_names = []	
    for i in distances[1:6]:
        recommended_movie_names.append(movies.iloc[i[0]].title)
    return recommended_movie_names

movies = pd.read_pickle('Movies_list.pkl')
similarity = pd.read_pickle(open('similarity.pkl','rb'))

st.title("Movie recommender system")

selected_movie = st.selectbox("Type a movie name",movies['title'].values)

if st.button("Get recommendation"):
	recommendations = recommend(selected_movie)
	for i in recommendations:
		st.write(i)
	
