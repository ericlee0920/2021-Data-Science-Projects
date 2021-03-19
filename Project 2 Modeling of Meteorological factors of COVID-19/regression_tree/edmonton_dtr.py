import pandas as pd

from regression_tree import *

# Import the Edmonton Factors Dataset
EDMONTON_DATA = pd.read_csv(r'C:\Chung\URO\covid-factors\datasets\Edmonton_Factors.csv')

edmonton_dtr = RegressionTree(EDMONTON_DATA)
edmonton_dtr.regression_tree()
edmonton_dtr.get_feature_importance("Edmonton")
edmonton_dtr.get_viz('edmonton_dtr.dot')
