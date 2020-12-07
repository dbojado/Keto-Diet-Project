# Acquire File
# Imports

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
import os

################### Acquire Nutritional Facts Data #####################

def get_nutrition_data():
    # Acquire data
    df = pd.read_csv('nutrition.csv')
    return df

