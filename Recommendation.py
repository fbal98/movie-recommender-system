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
        self.encodedData = pickle.load(open('assets/encodedData', 'rb'))
        self.data = pickle.load(open('assets/data', 'rb'))
        self.model = pickle.load(open('assets/model', 'rb'))

    def findMatching(self, query):
        matchingList = []

        i = 0

        for row in self.data.itertuples():
            title = row[2]
            tag = row[6]
            index = row.Index

            if fuzz.partial_ratio(title, query) > 30:
                matchingList.append(self.encodedData[index])

            if fuzz.partial_ratio(tag, query) > 30:
                matchingList.append(self.encodedData[index])

        return matchingList

    def make_recommendation(self,favoriteMovies):
        PredictionList = []

        for i in range(len(favoriteMovies)):
            PredictionList.extend(self.findMatching(favoriteMovies[i]))

        _, predicted = self.model.kneighbors(PredictionList, n_neighbors=9)

        return self.data.iloc[predicted[0]]








##how to use it

#
# r = Recommendation()
# #
# r.findMatching(["shawshanl"])
# predictedMoviesList = r.make_recommendation(["shawshank redemption", 'the matrix', 'inception', 'dark Knight'])
# #
# print(predictedMoviesList.values.tolist())
# #

#
# encodedData = pickle.load(open('assets/encodedData', 'rb'))
# data = pickle.load(open('assets/data', 'rb'))
# model = pickle.load(open('assets/model', 'rb'))
#



# print(type(data))