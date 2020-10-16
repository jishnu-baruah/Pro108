import csv
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import statistics

df = pd.read_csv('./Pro108/data.csv')
ratingList = df['Avg Rating'].tolist()


fig = ff.create_distplot([ratingList], ['Average Rating'])
fig.show()
