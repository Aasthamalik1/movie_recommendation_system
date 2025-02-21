import pandas as pd
import numpy as np
import ast
from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem.porter import PorterStemmer
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import streamlit as st
#loading our raw dataset
movies=pd.read_csv('tmdb_5000_movies.csv')
credits=pd.read_csv('tmdb_5000_credits.csv')

#preprocessing phase

#1: merging the two csv files ie movies and credits to form a single dataset
movies=movies.merge(credits,on='title')
#2: feature selection --> selecting only those data features which we require
movies=movies[['genres','keywords','overview','title','cast','crew','id']]
#3: data cleaning
    #3.1:droping null values
movies.dropna(inplace=True)

def convert(obj):
    l=[]
    for i in ast.literal_eval(obj):
        l.append(i['name'])
    return l
  #3.2 extracting only releveant data from genres keywords ,cast and crew
movies['genres']=movies['genres'].apply(convert)
movies['keywords']=movies['keywords'].apply(convert)

def convert3(obj):
    l=[]
    count=0
    for i in ast.literal_eval(obj):
        if count!=3:
            l.append(i['name'])
            count=count+1
        else:
            break
    return l
movies['cast']=movies['cast'].apply(convert3)
      
def fetch_director(obj):
    l=[]
    for i in ast.literal_eval(obj):
        if i['job']=='Director':
           l.append(i['name'])
           break
    return l
movies['crew']=movies['crew'].apply(fetch_director)
#3.3 converting overview into a dictionary
movies['overview']=movies['overview'].apply(lambda x:x.split())

#3.4 removing extra spaces
movies['genres']=movies['genres'].apply(lambda x:[i.replace(" ","") for i in x])
movies['keywords']=movies['keywords'].apply(lambda x:[i.replace(" ","") for i in x])
movies['cast']=movies['cast'].apply(lambda x:[i.replace(" ","") for i in x])
movies['crew']=movies['crew'].apply(lambda x:[i.replace(" ","") for i in x])
#3.5 adding a new column tag 
movies['tags']=movies['overview']+movies['genres']+movies['keywords']+movies['cast']+movies['crew']
#3.6 creating the final dataset designed according to our requirements
new = movies.drop(columns=['overview','genres','keywords','cast','crew'])
new['tags'] = new['tags'].apply(lambda x: " ".join(x))

cv = CountVectorizer(max_features=5000,stop_words='english')
vector = cv.fit_transform(new['tags']).toarray()
similarity = cosine_similarity(vector)

def recommend(movie):
    movie = movie.lower().strip()  
    new['title'] = new['title'].str.lower().str.strip()  
    matching_movies = new[new['title'].str.contains(movie, case=False, na=False)]
    index_list = new[new['title'] == movie].index.tolist()
    index = index_list[0]  # Get first index
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    for i in distances[1:6]:
        print(new.iloc[i[0]].title)

pickle.dump(new.to_dict(),open('movies.pkl','wb'))

pickle.dump(similarity ,open('similarity .pkl','wb'))