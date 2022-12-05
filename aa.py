import csv
from dash import Dash, dcc, html, Input, Output, State
from sklearn import datasets
from sklearn.svm import SVC
import pandas as pd

df = pd.read_csv('data.csv')
iris = datasets.load_iris()
clf = SVC()
clf.fit(iris.data, iris.target_names[iris.target])

app = Dash(__name__)

app.layout = html.Div([
    html.Label("Input Temperature : "), dcc.Input(id='input-on-submit1', type='text'),
    html.Br(),
    html.Label("Input Humidity : "), dcc.Input(id='input-on-submit2', type='text'),
    html.Br(),
    html.Label("Input Outlook : "),dcc.Dropdown(['overcast', 'rainy','sunny' ], '-', id='demo-dropdown1'),
     html.Div(id='dd-output-container1'),
    html.Br(),
    html.Label("Input Windy : "),dcc.Dropdown(['FALSE', 'TRUE', ], '-', id='demo-dropdown2'),
     html.Div(id='dd-output-container2'),
    html.Br(),
    html.Button('Submit', id='submit-val', n_clicks=0),
    html.Br(),
    html.Div(id='container-button-basic',
             children='Enter a value and press submit')
])


@app.callback(
    Output('container-button-basic', 'children'),
    Input('submit-val', 'n_clicks'),
    State('input-on-submit1', 'value'),
    State('input-on-submit2', 'value'),
    State('demo-dropdown1', 'value'),
    State('demo-dropdown2', 'value')
)
def update_output(n_clicks, value1, value2, value3, value4):
    test1 = [value1, value2, value3, value4]
    
    
    return 'ผลการทำนาย คือ ::  {} '.format(
        list(clf.predict( [test1] ))
    )

if __name__ == '__main__':
    app.run_server(debug=True)