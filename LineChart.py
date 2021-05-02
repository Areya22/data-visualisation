#LINE CHART
import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
print("Setup Complete")
import os
if not os.path.exists("../input/museum_visitors.csv"):
    os.symlink("../input/data-for-datavis/museum_visitors.csv", "../input/museum_visitors.csv") 
from learntools.core import binder
binder.bind(globals())
from learntools.data_viz_to_coder.ex2 import *
print("Setup Complete")

museum_filepath = "../input/museum_visitors.csv"
museum_data = pd.read_csv(museum_filepath, index_col="Date", parse_dates=True)
step_1.check()
museum_data.tail() 

# Fill in the line below: How many visitors did the Chinese American Museum 
# receive in July 2018?
ca_museum_jul18 = 2620 

# Fill in the line below: In October 2018, how many more visitors did Avila 
# Adobe receive than the Firehouse Museum?
avila_oct18 = 14658

# Line chart showing the number of visitors to each museum over time
sns.lineplot(data=museum_data) 

sns.lineplot(data=museum_data['Avila Adobe'],label='Avila Adobe')