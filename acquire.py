# Acquire File
# Imports

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
import os

################### Acquire Nutritional Facts Data #####################

def get_nutrition_data(cached=False):
    '''
    This function reads nutrition data if cached == False
    or if cached == True reads in nutrition data df from a csv file, returns df
    '''
    if cached or os.path.isfile('nutrition.csv') == False:
        df = nutrition()
    else:
        df = pd.read_csv('nutrition.csv')
    return df

