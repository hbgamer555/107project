import pandas as pd
import csv
import plotly.graph_objects as go

df=pd.read_csv(r"C:\Users\ADMIN\Dropbox\My PC (DESKTOP-QH1TBQA)\Downloads\New folder (5)\Data-visualization-master\csv files\data5.csv")
print(df.groupby("level")["attempt"].mean())
fig=go.Figure(go.Bar(x=df.groupby("level")["attempt"].mean(),y=['level1','level2','level3','level4'],orientation='h'))
fig.show()
