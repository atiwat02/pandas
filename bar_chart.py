from dash import Dash, dash_table
import plotly.express as px
import pandas as pd

df = pd.read_csv('data.csv')

app = Dash(__name__)

fig = px.bar(df, x='Outlook', y='Temperature',color='Play', barmode='group',)
fig.show()

if __name__ == '__main__':
    app.run_server(debug=True)
