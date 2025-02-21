# Movie Recommendation System

## Overview

This is a Movie Recommendation System built using Python, Pandas, Scikit-learn, and Streamlit.
The system recommends movies based on content similarity by analyzing genres, keywords, cast, crew, and overviews of movies.

## Features

Preprocesses movie data from the TMDB 5000 dataset.

Extracts relevant features (genres, keywords, cast, and crew).

Creates a movie recommendation model using CountVectorizer and cosine similarity.

Allows users to select a movie and get top 5 similar movie recommendations.

Implements Streamlit for an interactive UI.

## Installation & Setup

### Prerequisites

Make sure you have Python 3.10+ installed.

### Step 1: Clone the Repository

git clone https://github.com/Aasthamalik1/movie_recommendation_system
cd movie-recommendation-system

### Step 2: Create & Activate Virtual Environment

python -m venv venv  # Create virtual environment
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate  # For Windows

### Step 3: Install Dependencies

pip install -r requirements.txt

### Step 4: Run the Preprocessing Script

python preprocess.py

This script processes the dataset, generates movies.pkl and similarity.pkl, and saves them for later use.

### Step 5: Run the Streamlit App

streamlit run app.py

### File Structure

movie-recommendation-system/
│-- app.py               # Streamlit application
│-- preprocess.py        # Data processing & model training
│-- tmdb_5000_movies.csv # Dataset
│-- tmdb_5000_credits.csv
│-- movies.pkl           # Processed movie data
│-- similarity.pkl       # Cosine similarity matrix
│-- requirements.txt     # Dependencies
│-- README.md            # Project documentation

## How It Works

The preprocessing script merges and cleans the dataset.

It extracts relevant movie features like genres, keywords, cast, crew, and overview.

The text data is converted into feature vectors using CountVectorizer.

A cosine similarity matrix is created to measure how similar movies are to each other.

The Streamlit app allows users to select a movie and get recommendations.

🚀 Enjoy recommending movies! 🎬
