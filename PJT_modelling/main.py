# import

import pandas as pd

from catboost import CatBoostRegressor

from processing import checkNaN, dropNaN
from featuring import *
from modelling import fit_model

def main() :
    print("Data loading...")
    train = pd.read_csv("../input/pubg-finish-placement-prediction/train_V2.csv")
    test = pd.read_csv("../input/pubg-finish-placement-prediction/test_V2.csv")
    print("Data loaded!")
    
    # pre-processing train
    checkNaN(train)
    train = dropNaN(train)
    train = dropOutlier(train)
    train = encodeMatch(train)
    train = makeCols(train)
    train = train.drop(["Id","groupId", "matchType","matchId", "numGroups","damageDealt"], axis=1) 
    
    # pre-processing test
    test = encodeMatch(test)
    test = makeCols(test)
    test = test.drop(["Id","groupId", "matchType","matchId", "numGroups","damageDealt"], axis=1) 
    
    X = train.drop(["winPlacePerc"], axis=1)
    y = train['winPlacePerc']
    
    model = CatBoostRegressor(iterations=40, depth=16, learning_rate=1, loss_function='MAE')
    model.fit(X, y)
    
    result = model.predict(test)
    
    sample_submission = pd.read_csv("../input/pubg-finish-placement-prediction/sample_submission_V2.csv",index_col = "Id")
    sample_submission["winPlacePerc"] = result
    sample_submission.to_csv("submission.csv")

if __name__=="__main__" :
    main()

