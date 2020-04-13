import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go

app = dash.Dash()

# loading the dataset
df = pd.read_csv('./iris.csv')

# extracting only column except the last column
features = df.columns[:-1]

# setting up the app layout
app.layout = html.Div([
    # first dropdown list
    html.Div([
        dcc.Dropdown(id='xaxis',
                     options=[{'label': i, 'value': i} for i in features],
                     value='sepal_length'
                     )
    ],
        style={'width': '48%', 'display': 'inline-block'}),
    # second dropdown list
    html.Div([
        dcc.Dropdown(id='yaxis',
                     options=[{'label': i, 'value': i}for i in features],
                     value='petal_length'
                     )
    ],
        style={'width': '48%', 'display': 'inline-block'}),

    # actual scatter plot graph
    dcc.Graph(id='graphs')

], style={'padding': 10})


# Callback function
@app.callback(Output('graphs', 'figure'),
              [Input('xaxis', 'value'),
               Input('yaxis', 'value')])
# Function that update changes based on selected input
def update_graph(xname, yname):

    trace = []
    for species in df['species'].unique():
        # first plot
        if species == 'setosa':
            trace.append(go.Scatter(
                x=df[xname][0:52],
                y=df[yname][0:52],
                mode='markers',
                name='setosa',
                opacity=0.7,
                marker={'size': 15, 'opacity': 1, 'line': {
                    'width': 0.5, 'color': 'white'}}
            ))
        # Second plot
        if species == 'versicolor':
            trace.append(go.Scatter(
                x=df[xname][53:102],
                y=df[yname][53:102],
                mode='markers',

                name='virginica',
                opacity=0.7,
                marker={'size': 15, 'opacity': 1, 'line': {
                    'width': 0.5, 'color': 'white'}}
            ))
        # Third plot
        if species == 'virginica':
            trace.append(go.Scatter(
                x=df[xname][102:],
                y=df[yname][102:],
                mode='markers',

                name='versicolor',
                opacity=0.7,
                marker={'size': 15, 'opacity': 1, 'line': {
                    'width': 0.5, 'color': 'white'}}
            ))

    return {'data': trace,
            'layout': go.Layout(title='Iris dataset',
                                xaxis=dict(title=xname),
                                yaxis=dict(title=yname),
                                hovermode='closest'
                                )}


if __name__ == "__main__":
    app.run_server()
