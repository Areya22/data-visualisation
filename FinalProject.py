#FINAL PROJECT

import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
print("Setup Complete")
from learntools.core import binder
binder.bind(globals())
from learntools.data_viz_to_coder.ex7 import *
print("Setup Complete")

my_filepath = "../input/breast-cancer-prediction-dataset/Breast_cancer_data.csv"
my_data = pd.read_csv(my_filepath, header=0)
my_data.head()
my_data.diagnosis.unique()
my_data['diagnosis'] = my_data['diagnosis'].map({'M':1,'B':0})
sns.barplot(my_data['diagnosis'])
