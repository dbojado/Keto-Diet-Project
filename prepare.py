# Prepare File
# Imports

import pandas as pd
import numpy as np
import scipy as sp 
import matplotlib.pyplot as plt
import seaborn as sns
import os

from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, QuantileTransformer, PowerTransformer, RobustScaler, MinMaxScaler

################### Prepare Nutritional Facts Data #####################

def clean_nutrition_data():
    # Drop any duplicates in data
    df.drop_duplicates(inplace=True)

    # Drop unnecessary columns
    df = df.drop(columns=cols_to_drop)
    df = prepare.data_prep(df,cols_to_remove=['id'],
    prop_required_column=.6,
    prop_required_row=.75)

    # Handle missing values
    df = df.dropna(axis=1, thresh=threshold, inplace=True)

    # Specific removal of outliers
    # df = df[]
    # return df

def prep_nutrition_data():
    df = clean_data()
    train_validate, test = train_test_split(df, test_size=.3, random_state=123)
    train, validate = train_test_split(train_validate, test_size=.2, random_state=123)
    return train, validate, test

