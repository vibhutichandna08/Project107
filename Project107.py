import pandas as p
import plotly.express as px
import csv

df = p.read_csv('Project107_data.csv')
sdf = df.groupby(["student_id", "level"], as_index=False)["attempt"].mean()
fig = px.scatter(sdf, x='student_id', y='level', color='attempt',size='attempt')
fig.show()
