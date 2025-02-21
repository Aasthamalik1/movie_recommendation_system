import pickle
import streamlit as st
import pandas as pd

movies=pickle.load(open('movies.pkl','rb'))
similarity =pickle.load(open('similarity .pkl','rb'))
movies_list=pd.DataFrame(movies)
st.title("MOVIE RECOMMENDAR SYSTEM")

def recommend(movie):
    movie = movie.lower().strip()  
    movies_list['title'] = movies_list['title'].str.lower().str.strip()  
    matching_movies = movies_list[movies_list['title'].str.contains(movie, case=False, na=False)]
    index_list = movies_list[movies_list['title'] == movie].index.tolist()
    index = index_list[0]  # Get first index
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommend_movies=[]
    for i in distances[1:6]:
        recommend_movies.append(movies_list.iloc[i[0]].title)
    return recommend_movies


option=st.selectbox("Select a movie:", movies_list['title'].values)
if st.button("Recommend"):
   recommendations=recommend(option)
   for i in recommendations:
    st.write(i)

