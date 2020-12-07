# Prepare File
# Imports

import pandas as pd
import numpy as np
import scipy as sp 
import matplotlib.pyplot as plt
import seaborn as sns
import os

from sklearn.model_selection import train_test_split

################### Prepare Nutritional Facts Data #####################

def wrangle_nutrition_data(): 
    # Acquire data
    df = pd.read_csv('nutrition.csv')

    # Drop any duplicates in data
    df.drop_duplicates(inplace=True)

  # Drop unnecessary columns
    df = df.drop(['number', 'serving_size', 'saturated_fat','cholesterol','sodium','choline','folate','folic_acid','niacin','pantothenic_acid',
        'riboflavin','thiamin','vitamin_a','vitamin_a_rae','carotene_alpha','carotene_beta','cryptoxanthin_beta',
        'lutein_zeaxanthin','lucopene','vitamin_b12','vitamin_b6','vitamin_c','vitamin_d','vitamin_e','tocopherol_alpha',
        'vitamin_k','calcium','copper', 'iron','magnesium','manganese','phosphorous','potassium','selenium','zinc',
        'alanine','arginine','aspartic_acid','cystine','glutamic_acid','glycine','histidine','hydroxyproline','isoleucine',
        'leucine','lysine','methionine','phenylalanine','proline','serine','threonine','tryptophan','tyrosine','valine',
        'fiber', 'sugars','fructose','galactose','glucose','lactose','maltose','sucrose','fat','saturated_fatty_acids',
        'monounsaturated_fatty_acids','polyunsaturated_fatty_acids','fatty_acids_total_trans','alcohol','ash','caffeine',
        'theobromine','water'], axis = 1)
    # There are no missing values in the dataset
    # Decided to leave outliers because want to investigate them

    # Train, validate, and test
    train_validate, test = train_test_split(df, test_size=.3, random_state=123)
    train, validate = train_test_split(train_validate, test_size=.2, random_state=123)
   
   # Split into X and y
    X_train = train.drop(columns='total_fat')
    y_train = train[['total_fat']]

    # Validate split
    X_validate = validate.drop(columns='total_fat')
    y_validate = validate[['total_fat']]

    # Test split
    X_test = test.drop(columns='total_fat')
    y_test = test[['total_fat']]

    return df