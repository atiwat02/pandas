from dash import Dash, dcc, html, Input, Output, State
from sklearn import datasets
from sklearn.svm import SVC

iris = datasets.load_iris()
clf = SVC()
clf.fit(iris.data, iris.target_names[iris.target])

app = Dash(__name__)

app.layout = html.Div([
    html.Label("Input sepal length : "), dcc.Input(id='input-on-submit1', type='text'),
    html.Br(),
    html.Label("Input sepal width : "), dcc.Input(id='input-on-submit2', type='text'),
    html.Br(),
    html.Label("Input petal length : "), dcc.Input(id='input-on-submit3', type='text'),
    html.Br(),
    html.Label("Input petal width : "), dcc.Input(id='input-on-submit4', type='text'),
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
    State('input-on-submit3', 'value'),
    State('input-on-submit4', 'value')
)
def update_output(n_clicks, value1, value2, value3, value4):
    test1 = [value1, value2, value3, value4]
    
    
    return 'ผลการทำนาย คือ ::  {} '.format(
        list(clf.predict( [test1] ))
    )

if __name__ == "__main__":
    app.run_server(host='127.0.0.1', port='7080')   
