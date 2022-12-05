from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import pandas as pd
from dash import Dash, dash_table
import plotly.express as px


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H1('Dash Tabs component demo'),
    dcc.Tabs(id="tabs-example-graph", value='tab-1-example-graph', children=[
        dcc.Tab(label='Tab One', value='tab-1-example-graph'),
        dcc.Tab(label='Tab Two', value='tab-2-example-graph'),
        dcc.Tab(label='Tab Three', value='tab-3-example-graph'),
    ]),
    html.Div(id='tabs-content-example-graph')
])


@app.callback(Output('tabs-content-example-graph', 'children'),
              Input('tabs-example-graph', 'value'))
def render_content(tab):
    if tab == 'tab-1-example-graph':
        df = pd.read_csv('data.csv')
        return html.Div([
            html.H3('Tab content 1'),
            dash_table.DataTable(df.to_dict('records'), [
                                 {"name": i, "id": i} for i in df.columns])
        ])
    if tab == 'tab-2-example-graph':
        df = pd.read_csv('data.csv')
        fig = px.scatter(df, x="Temperature", y="Humidity", color="Play")
        return html.Div([
            html.H3('Tab content 2'),
            fig.show()
            
        ])
    elif tab == 'tab-3-example-graph':
        return html.Div([
            html.H3('Tab content 3'),
            dcc.Graph(
                id='graph-2-tabs-dcc',
                figure={
                    'data': [{
                        'x': [1, 2, 3],
                        'y': [5, 10, 6],
                        'type': 'dropdown'
                    }]
                }
            )
        ])


# from dash import Dash, dcc, html, Input, Output
# from sklearn.model_selection import train_test_split
# from sklearn import linear_model, tree, neighbors
# import plotly.graph_objects as go
# import plotly.express as px
# import numpy as np
# import pandas as pd

# df = pd.read_csv('data.csv')

# app = Dash(__name__)

# models = {'Regression': linear_model.LinearRegression,
#           'Decision Tree': tree.DecisionTreeRegressor,
#           'k-NN': neighbors.KNeighborsRegressor}

# app.layout = html.Div([
#     html.H4("Predicting restaurant's revenue"),
#     html.P("Select model:"),
#     dcc.Dropdown(
#         id='dropdown',
#         options=["Regression", "Decision Tree", "k-NN"],
#         value='Decision Tree',
#         clearable=False
#     ),
#     dcc.Graph(id="graph"),
# ])


# @app.callback(
#     Output("graph", "figure"),
#     Input('dropdown', "value"))
# def train_and_display(name):
#     df = pd.read_csv('data.csv') # replace with your own data source
#     X = df.Temperature.values[:, None]
#     X_train, X_test, y_train, y_test = train_test_split(
#         X, df.Humidity, random_state=42)

#     model = models[name]()
#     model.fit(X_train, y_train)

#     x_range = np.linspace(X.min(), X.max(), 100)
#     y_range = model.predict(x_range.reshape(-1, 1))

#     fig = go.Figure([
#         go.Scatter(x=X_train.squeeze(), y=y_train,
#                    name='train', mode='markers'),
#         go.Scatter(x=X_test.squeeze(), y=y_test,
#                    name='test', mode='markers'),
#         go.Scatter(x=x_range, y=y_range,
#                    name='prediction')
#     ])
#     return fig
if __name__ == '__main__':
    app.run_server(debug=True)
