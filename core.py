import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import tree, linear_model
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import os
import seaborn as sns

sns.set(style='white')
sns.set(style='whitegrid', color_codes=True)

from scipy.stats import linregress


class Admission_Predictor:

    def __init__(self):
        path = '/Users/robertmorrislike/BU_Study/EC601/SilverLobster/'
        os.chdir(path)
        self.data = pd.read_csv("Admission_Predict.csv")
        # Check Missing values
        # print((self.data.notnull().sum() / len(self.data)).sort_values(ascending=False))

    def model_decision(self):

        # data Pre - processing
        cols = self.data.columns
        features = cols[1:-1]
        target = cols[-1]

        X = self.data[features]
        y = self.data['Chance of Admit ']

        # train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.25)
        train_X = X[:int(0.75 * len(X))]
        test_X = X[int(0.75 * len(X)):]
        train_y = y[:int(0.75 * len(X))]
        test_y = y[int(0.75 * len(X)):]

        # Decision tree Regression
        self.model = DecisionTreeRegressor(max_leaf_nodes=10)
        self.model.fit(train_X, train_y)

        # Linear Model
        self.model2 = linear_model.LinearRegression()
        self.model2.fit(train_X, train_y)

        #print(self.model)
        #print(self.model2)
        # print(self.model3)

        # Visualization
        with open("classifier.dot", "w") as f:
            f = tree.export_graphviz(self.model, feature_names=features, class_names=target, out_file=f)

        # Test data Prediction
        self.predicted = self.model.predict(test_X)
        self.predicted_full = self.model.predict(X)
        self.score1 = self.model.score(test_X, test_y)
        #print("Score1: ", self.score1)
        print(self.score1)
        self.predicted_2 = self.model2.predict(test_X)
        self.predicted_full_2 = self.model2.predict(X)
        self.score2 = self.model2.score(test_X, test_y)
        #print("Score2: ", self.score2)
        print(self.score2)
        #print("Coefficients-----------", self.model2.coef_)
        #print("Intercept-----------", self.model2.intercept_)

        return self.score1,self.score2  # sample prediction


#ad = Admission_Predictor()

#train_X, test_X, train_y, test_y = ad.model_decision()
#ad.error_calc(test_y)
#ad.output_results()
#ad.plot_data(test_y)
