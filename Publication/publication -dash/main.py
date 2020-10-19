import dash  #(version 1.12.0)
from dash.dependencies import Input, Output
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import dash_auth

# -------------------------------------------------------------------------------------
# Import the cleaned data (importing csv into pandas)
df = pd.read_csv("pubEval.csv")

#print(df)




# -------------------------------------------------------------------------------------
# App layout
app = dash.Dash('auth') # this was introduced in Dash version 1.12.0

VALID_USERNAME_PASSWORD_PAIRS = [
    ['admin', 'admin']
]

auth = dash_auth.BasicAuth(
    app,
    VALID_USERNAME_PASSWORD_PAIRS
)

app.layout = html.Div([
    html.H1(
        children='Welcome to System and Computer Engineering Publication ',
        style={
            'textAlign': 'center',
            'color':'red'
        }
    ),

    html.Div(children='Find the SCE Publication Data as below', style={
        'textAlign': 'center'
    }),
    html.Br(),

    dcc.Dropdown(
        id='dropdown',
        options=[{'label': i, 'value': i} for i in ['LA', 'NYC', 'MTL']],
        value='LA'
    ),
    html.Br(),
    html.Div(id='display-value'),
    html.Br(),
    html.H2(
        children='Find the Table below  ',
        style={
            'textAlign': 'center'
        }
    ),





])

#----------------------------------------------------------------------------
#callback

@app.callback(dash.dependencies.Output('display-value', 'children'),
              [dash.dependencies.Input('dropdown', 'value')])
def display_value(value):
    return 'You have selected "{}"'.format(value)


'''
    dash_table.DataTable(
        id='datatable',
        columns=[

        ],
        data=df.to_dict('records'),
        sort_action="native",
        page_action="native",       # all data is passed to the table up-front or not ('none')
        page_current=0,             # page number that user is on
        page_size=6,                # number of rows visible per page

        style_cell={                # ensure adequate header width when text is shorter than cell's text
            'minWidth': 95, 'maxWidth': 95, 'width': 95
        },

                         )
    '''



# -------------------------------------------------------------------------------------

if __name__ == '__main__':
    app.run_server(debug=True)




