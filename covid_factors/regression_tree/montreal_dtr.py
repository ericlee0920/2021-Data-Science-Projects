import pandas as pd

from regression_tree import *

# Import the Montreal Factors Dataset
MONTREAL_DATA = pd.read_csv(r'C:\Chung\URO\covid-factors\datasets\Montreal_Factors.csv')

montreal_dtr = RegressionTree(MONTREAL_DATA)
montreal_dtr.regression_tree()
montreal_dtr.get_feature_importance("Montreal")
montreal_dtr.get_viz('montreal_dtr.dot')
