import sys

import sklearn
from sklearn.neighbors import KNeighborsClassifier
import sklearn.neighbors
import pandas as pd
import numpy as np
import pickle
from fuzzywuzzy import fuzz

class Recommendation:


    def __init__(self):
        # importing data and model
        self.user_movie_df = pickle.load(open('assets/user_movie_df', 'rb'))
        self.movieTitles = pickle.load(open('assets/movieTitles', 'rb'))

    def findMatching(self, query):
        matching = None
        for row in self.movieTitles.itertuples():

            if fuzz.partial_ratio(row[1].lower(), query) > 80:
                matching = row[1]
                break

        if matching:
            return matching
        else:
            return None

    def make_recommendation(self,favoriteMovie):

        matching = self.findMatching(favoriteMovie)
        if matching is None:
            return None
        else:
            movie_name = self.user_movie_df[matching]

            return self.user_movie_df.corrwith(movie_name).sort_values(ascending=False)[1:6].to_json()


