#install dependencies
!pip install matplotlib
!pip install pandas
!pip install numpyimport

#import libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

#load data (using unzip folder path subdirectory)
image_df = pd.read_csv('index_ade20k_csv/ADE20K_index_image.csv')

# Explore data

# Look at image_df columns
print('\x1b[34mImage_df Columns:\x1b[0m')
print(image_df.head(2))
print('\n')

# Look at filename list
print('\x1b[34mImage_df Filename List:\x1b[0m')
print(image_df['filename'].values)
print('\n')

# Count number of scenes
print('\x1b[34mImage_df Scene Counts:\x1b[0m')
[print(str(i)) for i in Counter(image_df['scene'].values).most_common(15)];