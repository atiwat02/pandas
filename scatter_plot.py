from dash import Dash, dash_table
import plotly.express as px
import pandas as pd

df = pd.read_csv('data.csv')
print([[df["Temperature"]]])
app = Dash(__name__)

fig = px.scatter(df, x="Temperature", y="Humidity", color="Play")
fig.show()

if __name__ == '__main__':
    app.run_server(debug=True)

