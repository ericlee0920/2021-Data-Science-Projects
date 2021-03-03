import pandas as pd

from regression_tree import *

# Import the Toronto Factors Dataset
TORONTO_DATA = pd.read_csv(r'C:\Chung\URO\covid-factors\datasets\Edmonton_Factors.csv')

toronto_dtr = RegressionTree(TORONTO_DATA)
toronto_dtr.regression_tree()
toronto_dtr.get_feature_importance("Toronto")
toronto_dtr.get_viz('toronto_dtr.dot')
