from dash import Dash, dash_table
import plotly.express as px
import pandas as pd

df = pd.read_csv('data.csv')

app = Dash(__name__)


app.layout = dash_table.DataTable(df.to_dict('records'), [{"name": i, "id": i} for i in df.columns])

if __name__ == '__main__':
    app.run_server(host='127.0.0.1',port='8080')


