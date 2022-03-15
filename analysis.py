import pandas as pd
import plotly.graph_objects as go

file=pd.read_csv('data.csv')
student_data = file.loc[file['student_id']=='TRL_987']
analysis= student_data.groupby('level')['attempt'].mean()
print(analysis)

fig = go.Figure(go.Bar(
    x=analysis,
    y=['Level 1' , 'Level 2' , 'Level 3', 'Level 4'],
    orientation='h'
))

fig.show()