import pandas as pd
import sklearn
import sklearn.model_selection
from sklearn.ensemble import RandomForestClassifier

class Supervised_learning(object):
    def __init__(self, workspace_dir):
        self.workspace_dir = workspace_dir
        self.df = pd.read_csv(workspace_dir+r'\\storage\\kag_risk_factors_cervical_cancer.csv')
        
    def run(self):
        print("run")
        train, test = sklearn.model_selection.train_test_split(self.df, test_size = 0.3, random_state = 123)
        train = pd.DataFrame(train)
        test = pd.DataFrame(test)
        print(train.describe(include= "all"))
        mdl = RandomForestClassifier(n_estimators = 100, max_depth = 2, random_state = 123)
        #mdl.fit()
