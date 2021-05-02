#DISTRIBUTION
import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
print("Setup Complete")
import os
if not os.path.exists("../input/cancer_b.csv"):
    os.symlink("../input/data-for-datavis/cancer_b.csv", "../input/cancer_b.csv")
    os.symlink("../input/data-for-datavis/cancer_m.csv", "../input/cancer_m.csv")
from learntools.core import binder
binder.bind(globals())
from learntools.data_viz_to_coder.ex5 import *
print("Setup Complete")

cancer_b_filepath = "../input/cancer_b.csv"
cancer_m_filepath = "../input/cancer_m.csv"

# Fill in the line below to read the (benign) file into a variable cancer_b_data
cancer_b_data = pd.read_csv(cancer_b_filepath, index_col="Id")

# Fill in the line below to read the (malignant) file into a variable cancer_m_data
cancer_m_data = pd.read_csv(cancer_m_filepath, index_col="Id")

cancer_b_data.head()
cancer_m_data.head()

# largest value for 'Perimeter (mean)'?
max_perim = 87.46

# Fill in the line below: What is the value for 'Radius (mean)' for the tumor with Id 842517?
mean_radius = 20.57

# Histograms for benign and maligant tumors
sns.distplot(a=cancer_b_data['Area (mean)']) # Your code here (benign tumors)
sns.distplot(a=cancer_m_data['Area (mean)']) # Your code here (malignant tumors)

# KDE plots for benign and malignant tumors
sns.kdeplot(data=cancer_b_data['Radius (worst)'], shade=True) # Your code here (benign tumors)
sns.kdeplot(data=cancer_m_data['Radius (worst)'], shade=True) # Your code here (malignant tumors)
