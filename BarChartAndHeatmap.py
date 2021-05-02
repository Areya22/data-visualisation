#BAR CHART AND HEATMAP
import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
print("Setup Complete")
import os
if not os.path.exists("../input/ign_scores.csv"):
    os.symlink("../input/data-for-datavis/ign_scores.csv", "../input/ign_scores.csv") 
from learntools.core import binder
binder.bind(globals())
from learntools.data_viz_to_coder.ex3 import *
print("Setup Complete")

ign_filepath = "../input/ign_scores.csv"
ign_data = pd.read_csv(ign_filepath, index_col="Platform")
ign_data
# Fill in the line below: What is the highest average score received by PC games,
# for any platform?
high_score = 7.759930

# Fill in the line below: On the Playstation Vita platform, which genre has the 
# lowest average score? Please provide the name of the column, and put your answer 
# in single quotes (e.g., 'Action', 'Adventure', 'Fighting', etc.)
worst_genre = 'Simulation'

sns.barplot(x=ign_data.index, y=ign_data['Racing']) # Your code here
sns.heatmap(data=ign_data, annot=True) # Your code here
