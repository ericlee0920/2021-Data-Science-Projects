import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.tree import export_graphviz
from sklearn import metrics
import statsmodels.api as sm



class RegressionTree:

    def __init__(self, data):
        self.data = data
        self.x = data[["Mean Temp (C)", "Total Precip (mm)", "Avg Rel Hum (%)", "Avg Wind Spd (km/h)",
                       "Mean UV"]]
        self.y = data[["Cases"]]
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(self.x, self.y, test_size=0.3,
                                                                                random_state=0)
        self.DtReg = None

    def regression_tree(self):
        self.set_DtReg(DecisionTreeRegressor(max_depth=10, min_samples_split=3, min_samples_leaf=1, random_state=0))
        self.DtReg.fit(self.x_train, self.y_train)
        y_predict_dtr = self.DtReg.predict(self.x_test)
        r_square = metrics.r2_score(self.y_test, y_predict_dtr)
        print("R-Squared: ", r_square)

    def get_feature_importance(self, name):
        # get importance
        importance = self.DtReg.feature_importances_

        # summarize feature importance
        for i, v in enumerate(importance):
            print('Feature: %s Score: %.5f' % (i, v))

        # plot feature importance
        plt.figure(figsize=(10, 5))
        plt.title(name + " Feature Importances")
        plt.bar([x for x in range(len(importance))], importance)
        plt.xticks(range(self.x.shape[1]), ["Mean Temp (C)", "Total Precip (mm)", "Avg Rel Hum (%)",
                                            "Avg Wind Spd (km/h)", "Mean UV"])
        plt.show()

        # print(model.feature_importances_)  # use inbuilt class feature_importances of tree based classifiers
        # # plot graph of feature importances for better visualization
        # feat_importances = pd.Series(model.feature_importances_, index=X.columns)
        # feat_importances.nlargest(10).plot(kind='barh')
        # plt.show()

    def get_viz(self, out_file):
        # Store the decision tree in a tree.dot file to visualize plot
        # Visualize on webgraphviz.com by cping related data from dtregression.dot file

        export_graphviz(self.DtReg, out_file=out_file, feature_names=["Mean Temp (C)",
                        "Total Precip (mm)", "Avg Rel Hum (%)", "Avg Wind Spd (km/h)", "Mean UV"])

    def get_summary(self):
        X2 = sm.add_constant(self.x_test)
        est = sm.OLS(self.y_test, X2)
        est2 = est.fit()
        print(est2.summary())

    def get_data(self):
        return self.data

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_x_train(self):
        return self.x_train

    def get_x_test(self):
        return self.x_test

    def get_y_train(self):
        return self.y_train

    def get_y_test(self):
        return self.y_test

    def get_DtReg(self):
        return self.DtReg

    def set_DtReg(self, DtReg):
        self.DtReg = DtReg

    # def regression_tree_plt(self):
    #     X_val = np.arange(min(self.x_train), max(self.x_train))
    #
    #     # Reshape the data into a len(X_val)*1 array in order to make a column out of the X_val values
    #     X_val = X_val.reshape((len(X_val), 1))
    #
    #     # Define a scatter plot for training data
    #     plt.scatter(self.x_train, self.y_train, color='blue')
    #
    #     # Plot predicted data
    #     plt.plot(X_val, self.DtReg.predict(X_val), color='red')
    #
    #     # Define title
    #     plt.title("COVID Cases prediction using DTR")
    #
    #     # Define Y axis
    #     plt.ylabel('Number of Covid Cases')
    #
    #     plt.show()

