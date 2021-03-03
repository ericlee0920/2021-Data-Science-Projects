import pandas as pd

from regression_tree import *

# Import the Peel Factors Dataset
PEEL_DATA = pd.read_csv(r'C:\Chung\URO\covid-factors\datasets\Edmonton_Factors.csv')

peel_dtr = RegressionTree(PEEL_DATA)
peel_dtr.regression_tree()
peel_dtr.get_feature_importance("Peel")
peel_dtr.get_viz('peel_dtr.dot')
