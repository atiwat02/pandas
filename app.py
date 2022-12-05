import dash_bootstrap_components as dbc
from dash import html
import dash
from dash import Dash, dcc, html, Input, Output,State
from sklearn import tree
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LinearRegression

app = dash.Dash(__name__)
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
# df = pd.read_csv('heart.csv')
# newdf = df.drop(['oldpeak', 'slp', 'caa', 'thall'],axis=1)
# X = df[['age', 'sex', 'cp', 'trtbps', 'chol', 'fbs', 'restecg', 'thalachh','exng']]
# y = df['output']
# X_train,X_test,y_train,y_test = train_test_split(X,y,train_size=0.7)
# model = LinearRegression()
# model.fit(X_train,y_train)
# model.score(X_train,y_train)
# model.intercept_


app = dash.Dash(__name__)
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
badges = html.Div(
    [
    html.H1("Heart Attack PreDict by Jappyx" ,style={'background':'linear-gradient(90deg, RGBA( 0, 255, 255, 1 ) 0%, RGBA( 0, 0, 255, 1 ) 100%)','height' :100,'text-align': 'center','padding-top': '30px','border-radius':'25px'}),    
    ]
)
row_content = [
    dbc.Col(
            [
                
                dbc.Label("Age",),
                dbc.Input(
                    type="text",
                    id="input-on-submit1",
                ),     
            ],
            width=3,
        ),
        dbc.Col(
            [
                dbc.Label("Sex",),
                dbc.Input(
                    type="text",
                    id="input-on-submit2",
                ),
                dbc.FormText(
                    "0 = Male , 1 = Female",
                    color="secondary",
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
            style={'text-align':'center', 'margin':25},
        ),
    ],
)

row_content2 = [
    dbc.Col(
            [
                dbc.Label("Chest Pain type"),
                dbc.Select(id="input-on-submit3",options=[
                    {"label": "1: typical angina","value": "1"},
                    {"label": "2: atypical angina","value": "2"},
                    {"label": "3: non-anginal pain","value": "3"},
                    {"label": "4: asymptomatic","value": "4"},
                    ]),
              
            ],
            width=3,
        ),
        dbc.Col(
            [
                dbc.Label("Resting blood pressure (in mm Hg)"),
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
            style={'text-align':'center', 'margin':25},
        ),
    ],
    className="g-3",
)

row_content3 = [
    dbc.Col(
            [
                
                dbc.Label("Cholestoral in mg/dl fetched via BMI sensor",),
                dbc.Input(
                    type="text",
                    id="input-on-submit5",
                ),     
            ],
            width=3,
        ),
        dbc.Col(
            [
                dbc.Label("Fasting blood sugar > 120 mg/dl",),
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
            style={'text-align':'center', 'margin':25},
        ),
    ],
    className="g-3",
)


row_content4 = [
    dbc.Col(
            [
                
                dbc.Label("Resting electrocardiographic results"),
                dbc.Select(id="input-on-submit7",options=[
                    {"label": "0: normal","value": "0"},
                    {"label": "1: having ST-T wave abnormality","value": "1"},
                    {"label": "2: showing probable or definite left ventricular hypertrophy by Estes' criteria","value": "2"},
                    ]),

            ],
            width=3,
        ),
        dbc.Col(
            [
                dbc.Label("Maximum heart rate achieved",),
                dbc.Input(
                    type="text",
                    id="input-on-submit8",
                ),
            ],
            width=3,
        ),
]
re_input = dbc.Row(
    [
        dbc.Row(
            row_content4,
            justify="evenly",
            style={'text-align':'center', 'margin':25},
        ),
    ],
    className="g-3",
)

row_content4 = [
    dbc.Col(
            [
                
                dbc.Label("Exercise induced angina"),
                dbc.Select(id="input-on-submit9",options=[
                    {"label": "0: no","value": "0"},
                    {"label": "1: yes","value": "1"},
                    ]),

            ],
            width=3,
        ),
]
be_input = dbc.Row(
    [
        dbc.Row(
            row_content4,
            justify="evenly",
            style={'text-align':'center', 'margin':25},
        ),
    ],
    className="g-3",
)
button = html.Div(
    [
        dbc.Button("Predict", outline=True, n_clicks=0 ,color="info",id="submit-val", className="me-1"),
    ],
    className="d-grid gap-2 col-1 mx-auto",
    style={"width": "18rem", "bottom": "5rem"},
)

card = dbc.Card(
    dbc.CardBody(
        [
            html.H6(id='container-button-basic',
                children='Enter a value and press predict',
                style={'text-align':'center', 'margin':25},),
            
        ],
    ),
    style={"width": "18rem", "top": "3rem","background": "linear-gradient(90deg, RGBA( 0, 255, 255, 1 ) 31%, RGBA( 0, 0, 255, 1 ) 100%)",'border-radius':'25px'},
    className="d-grid gap-2 col-1 mx-auto",
)
score =html.Div([
    dbc.Card(
        dbc.CardBody(
            [   
                dbc.Label("Model score"),
                html.H4('0.4052714158008802'),
            ],
    ), 
    style={'text-align':'center',"width": "18rem", "top": "1rem","background": "linear-gradient(90deg, RGBA( 0, 255, 255, 1 ) 31%, RGBA( 0, 0, 255, 1 ) 100%)",'border-radius':'25px'},
    className="d-grid gap-3 col-1 mx-auto",
    ),
    dbc.Card(
        dbc.CardBody(
            [   
                dbc.Label("Model intercept"),
                html.H4('0.5679551262255362'),
            ],
    ),
    style={'text-align':'center',"width": "18rem", "top": "1rem","background": "linear-gradient(90deg, RGBA( 0, 255, 255, 1 ) 0%, RGBA( 0, 0, 255, 1 ) 100%)",'border-radius':'25px'},
    className="d-grid gap-3 col-1 mx-auto",
    )
    ],
    style ={"display":"flex",}
)
app.layout = dbc.Form([badges,score,email_input, password_input,de_input,re_input,be_input,button, card])

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
)
def update_output(n_clicks, value1, value2, value3,value4,value5,value6,value7,value8,value9):
    v1 = int(value1)
    v2 = int(value2)
    v3 = int(value3)
    v4 = int(value4)
    v5 = int(value5)
    v6 = int(value6)
    v7 = int(value7)
    v8 = int(value8)
    v9 = int(value9)
    # a = model.predict([[v1,v2,v3,v4,v5,v6,v7,v8,v9]])
    # if a < 0.3 :
    #     return "มีโอกาสเกิดโรคน้อย"
    # elif 0.3 < a <= 0.5 :
    #     return "มีโอกาสที่จะเกิด"
    # else :
    #     return "มีโอกาสเกิดสูง" 

if __name__ == "__main__":
    app.run_server(host='127.0.0.1', port='7050')