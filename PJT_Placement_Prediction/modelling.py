

# data set split and 4 models training
import numpy as np

from sklearn.linear_model import LinearRegression as linear
from sklearn.linear_model import Ridge as ridge
from sklearn.linear_model import Lasso as lasso
from xgboost.sklearn import XGBRFRegressor as xgboost
from lightgbm.sklearn import LGBMRegressor as lgbm
from catboost import CatBoostRegressor as catboost

from sklearn.model_selection import train_test_split

from sklearn.metrics import mean_absolute_error

def fit_model(df) :
    features = df.drop(["Id","groupId", "matchType","matchId", "numGroups","damageDealt","winPlacePerc"], axis=1) 
    target = df["winPlacePerc"]
    
    train_X, test_X, train_y, test_y = train_test_split(features, target, test_size=0.2, random_state=589)
    
    for model_func in [linear, ridge, lasso, lgbm, xgboost, catboost]:
      print(f"{model_func} Fitting...")
      model = model_func().fit(train_X, train_y)
      pred_y = model.predict(test_X)
      print("test MAE : ",np.round(mean_absolute_error(pred_y, test_y),6))
      pred_y = model.predict(train_X)
      print("train MAE : ",np.round(mean_absolute_error(pred_y, train_y),6))