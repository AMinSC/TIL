# data set split and 4 models training

def fit_model(df) :
    features = df.drop(["Id","groupId", "matchType","matchId", "numGroups","damageDealt","winPlacePerc"], axis=1) 
    target = df["winPlacePerc"]
    
    train_X, test_X, train_y, test_y = train_test_split(features, target, test_size=0.2, random_state=589)
    
    for model_func in [linear, ridge, lasso, lgbm]:
      print(f"{model_func} Fitting...")
      model = model_func().fit(train_X, train_y)
      pred_y = model.predict(test_X)
      print("test MAE : ",np.round(mean_absolute_error(pred_y, test_y),6))
      pred_y = model.predict(train_X)
      print("train MAE : ",np.round(mean_absolute_error(pred_y, train_y),6))