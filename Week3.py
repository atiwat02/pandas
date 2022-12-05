import dash_bootstrap_components as dbc
from dash import html
import dash
from dash import Dash, dcc, html, Input, Output, State
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

app = dash.Dash(__name__)
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

data = pd.read_csv('winequality-red.csv')

data['fixed_acidity'] = data.fixed_acidity.astype('category')
data['volatile_acidity'] = data.volatile_acidity.astype('category')
data['citric_acid'] = data.citric_acid.astype('category')
data['residual_sugar'] = data.residual_sugar.astype('category')
data['chlorides'] = data.chlorides.astype('category')
data['free_sulfur_dioxide'] = data.free_sulfur_dioxide.astype('category')
data['total_sulfur_dioxide'] = data.total_sulfur_dioxide.astype('category')
data['density'] = data.density.astype('category')
data['pH'] = data.pH.astype('category')
data['sulphates'] = data.sulphates.astype('category')
data['alcohol'] = data.alcohol.astype('category')

columns = ['fixed_acidity',	'volatile_acidity',	'citric_acid',	'residual_sugar',	'chlorides',	'free_sulfur_dioxide',	'total_sulfur_dioxide',	'density',	'pH',	'sulphates',	'alcohol']
X = data[ columns ].values
y = data['quality']

tree = DecisionTreeClassifier(criterion = "entropy")
tree.fit(X, y)

score = round((tree.score(X, y)*100),2)
Tscore = score,"%"

app = dash.Dash(__name__)
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

badges = html.Div(
    [
        html.H1("Wine Quality", 
                style={
                    'color': '#FFFFFF',
                    'background': '#FA3B15',
                    'height': 100,
                    'text-align': 'center',
                    'padding-top': '30px', 
                    'border-radius': '25px'
                    }
                ),
    ]
)

row_content = [
    dbc.Col(
        [
            dbc.Label("fixed_acidity",),
            dbc.Input(
                type="text",
                id="input-on-submit1",
            ),
        ],
        width=3,
    ),
    dbc.Col(
        [
            dbc.Label("volatile_acidity",),
            dbc.Input(
                type="text",
                id="input-on-submit2",
            ),
        ],
        width=3,
    ),
]

email_input = dbc.Row(
    [
        dbc.Row(
            row_content,
            justify="evenly",
            style={'text-align': 'center', 'margin': 25},
        ),
    ],
)

row_content2 = [
    dbc.Col(
        [
            dbc.Label("citric_acid",),
            dbc.Input(
                type="text",
                id="input-on-submit3",
            ),
        ],
        width=3,
    ),
    dbc.Col(
        [
            dbc.Label("residual_sugar",),
            dbc.Input(
                type="text",
                id="input-on-submit4",
            ),
        ],
        width=3,
    ),
]
password_input = dbc.Row(
    [
        dbc.Row(
            row_content2,
            justify="evenly",
            style={'text-align': 'center', 'margin': 25},
        ),
    ],
    className="g-3",
)

row_content3 = [
    dbc.Col(
        [
            dbc.Label("chlorides",),
            dbc.Input(
                type="text",
                id="input-on-submit5",
            ),
        ],
        width=3,
    ),
    dbc.Col(
        [
            dbc.Label("free_sulfur_dioxide",),
            dbc.Input(
                type="text",
                id="input-on-submit6",
            ),
        ],
        width=3,
    ),
]

de_input = dbc.Row(
    [
        dbc.Row(
            row_content3,
            justify="evenly",
            style={'text-align': 'center', 'margin': 25},
        ),
    ],
    className="g-3",
)

row_content4 = [
    dbc.Col(
        [
            dbc.Label("total_sulfur_dioxide",),
            dbc.Input(
                type="text",
                id="input-on-submit7",
            ),
        ],
        width=3,
    ),
    dbc.Col(
        [
            dbc.Label("density",),
            dbc.Input(
                type="text",
                id="input-on-submit8",
            ),
        ],
        width=3,
    ),
]

r_input = dbc.Row(
    [
        dbc.Row(
            row_content4,
            justify="evenly",
            style={'text-align': 'center', 'margin': 25},
        ),
    ],
    className="g-3",
)

row_content5 = [
    dbc.Col(
        [
            dbc.Label("pH",),
            dbc.Input(
                type="text",
                id="input-on-submit9",
            ),
        ],
        width=3,
    ),
    dbc.Col(
        [
            dbc.Label("sulphates",),
            dbc.Input(
                type="text",
                id="input-on-submit10",
            ),
        ],
        width=3,
    ),
]


re_input = dbc.Row(
    [
        dbc.Row(
            row_content5,
            justify="evenly",
            style={'text-align': 'center', 'margin': 25},
        ),
    ],
    className="g-3",
)

row_content6 = [
    dbc.Col(
        [
            dbc.Label("alcohol",),
            dbc.Input(
                type="text",
                id="input-on-submit11",
            ),
        ],
        width=3,
    ),
]

be_input = dbc.Row(
    [
        dbc.Row(
            row_content6,
            justify="evenly",
            style={'text-align': 'center', 'margin': 25},
        ),
    ],
    className="g-3",
)
button = html.Div(
    [
        dbc.Button(
            "Predict", 
            outline=True, n_clicks=0,
            color="info", id="submit-val", 
            className="me-1"
            ),
    ],
    className="d-grid gap-2 col-1 mx-auto",
    style={"width": "18rem", "bottom": "5rem"},
)

card = dbc.Card(
    dbc.CardBody(
        [
            html.H6(id='container-button-basic',
                    children='Enter a value and press predict',
                    style={'text-align': 'center', 'margin': 25},),
        ],
    ),
    style={
        "width": "18rem", 
        "top": "3rem",
        "background": "#04FCF8", 
        'border-radius': '25px'
        },
    className="d-grid gap-2 col-1 mx-auto",
)

score = html.Div([
    dbc.Card(
        dbc.CardBody(
            [
                dbc.Label("Model score"),
                html.H4(Tscore),
            ],
        ),
        style={
            'text-align': 'center', 
            "width": "18rem", 
            "top": "1rem",
            "background": "#04FCF8", 
            'border-radius': '25px'
            },
        className="d-grid gap-3 col-1 mx-auto",
    )
],
    style={"display": "flex", }
)
app.layout = dbc.Form(
    [
        badges, 
        score, 
        email_input, 
        password_input,
        de_input, 
        r_input,
        re_input, 
        be_input, 
        button, 
        card
    ]
    )


@app.callback(
    Output('container-button-basic', 'children'),
    Input('submit-val', 'n_clicks'),
    State('input-on-submit1', 'value'),
    State('input-on-submit2', 'value'),
    State('input-on-submit3', 'value'),
    State('input-on-submit4', 'value'),
    State('input-on-submit5', 'value'),
    State('input-on-submit6', 'value'),
    State('input-on-submit7', 'value'),
    State('input-on-submit8', 'value'),
    State('input-on-submit9', 'value'),
    State('input-on-submit10', 'value'),
    State('input-on-submit11', 'value'),
)
def update_output(n_clicks, value1, value2, value3, value4, value5, value6, value7, value8, value9, value10, value11):
    v1 = float(value1)
    v2 = float(value2)
    v3 = float(value3)
    v4 = float(value4)
    v5 = float(value5)
    v6 = float(value6)
    v7 = float(value7)
    v8 = float(value8)
    v9 = float(value9)
    v10 = float(value10)
    v11 = float(value11)
    
    p = tree.predict([[v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11]])
    result = "คุณภาพของไวน์ คือ :", p[0]
    print(result)
    return result

if __name__ == "__main__":
    app.run_server(host='127.0.0.1', port='7050')