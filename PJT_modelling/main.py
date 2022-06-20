# import

import pandas as pd

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

