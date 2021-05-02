#SCATTERPLOT
import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
print("Setup Complete")
import os
if not os.path.exists("../input/candy.csv"):
    os.symlink("../input/data-for-datavis/candy.csv", "../input/candy.csv") 
from learntools.core import binder
binder.bind(globals())
from learntools.data_viz_to_coder.ex4 import *
print("Setup Complete")
candy_filepath = "../input/candy.csv"

# Fill in the line below to read the file into a variable candy_data
candy_data = pd.read_csv(candy_filepath, index_col='id')
candy_data.head()

# Fill in the line below: Which candy was more popular with survey respondents:
# '3 Musketeers' or 'Almond Joy'?  (Please enclose your answer in single quotes.)
more_popular = '3 Musketeers'

# Fill in the line below: Which candy has higher sugar content: 'Air Heads'
# or 'Baby Ruth'? (Please enclose your answer in single quotes.)
more_sugar = 'Air Heads'

sns.scatterplot(x=candy_data['sugarpercent'], y=candy_data['winpercent']) # Your code here
sns.regplot(x=candy_data['sugarpercent'], y=candy_data['winpercent']) # Your code here
sns.scatterplot(x=candy_data['sugarpercent'], y=candy_data['winpercent'], hue=candy_data['chocolate']) # Your code here
sns.lmplot(x='sugarpercent', y='winpercent', hue='chocolate', data = candy_data) # Your code here
sns.swarmplot(x=candy_data['chocolate'],
              y=candy_data['winpercent'])
