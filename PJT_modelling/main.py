# import

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression as linear
from sklearn.linear_model import Ridge as ridge
from sklearn.linear_model import Lasso as lasso
from lightgbm import LGBMRegressor as lgbm
from lightgbm import plot_importance
import gc


from custfunc import reduce_ram_usage
from processing import checkNaN, dropNaN
from featuring import *
from modelling import fit_model

def main() :
    print("Data loading...")
    train = pd.read_csv("./data/train_V2.csv")
    test = pd.read_csv("./data/test_V2.csv")
    print("Data loaded!")
    
    checkNaN(train)
    train = dropNaN(train)
    
    train = dropOutlier(train)
    train = encodeMatch(train)
    train = makeCols(train)
    
    train = fit_model(train)

if __name__=="__main__" :
    main()


main()