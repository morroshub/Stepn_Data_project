import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Cargar el archivo CSV
df = pd.read_csv('Dash/Corridas-Stepn-PowerbiS.csv')
df['GMT'] = df['GMT'].fillna(0)

# Crear la aplicación Dash
app = dash.Dash(__name__)

# Definir el diseño de la aplicación
app.layout = html.Div([
    html.Div([
        html.H1('Dashboard 500 Days of Stepn by: @Mortadelamata'),
        html.Img(src='Dash/gmtlogo.jpg')
    ], className='banner'),

    html.Div([
        html.Div([
            html.P('Mined Assets', className='fix_label', style={'color': 'black', 'margin-top': '2px'}),
            dcc.RadioItems(
                id='radioitems',
                labelStyle={'display': 'inline-block'},
                options=[
                    {'label': 'GST', 'value': 'TOTAL FECHA GST'},
                    {'label': 'GMT', 'value': 'GMT'},
                ],
                value='TOTAL FECHA GST',
                style={'text-align': 'center', 'color': 'black'},
                className='dcc_compon'
            ),
        ], className='create_container2 five columns', style={'margin-bottom': '20px'}),
    ], className='row flex-display'),

    html.Div([
        html.Div([
            dcc.Graph(id='bar_graph', figure={})
        ], className='create_container2 eight columns'),

        html.Div([
            dcc.Graph(id='pie_graph', figure={})
        ], className='create_container2 five columns'),
    ], className='row flex-display')

], id='mainContainer', style={'display': 'flex', 'flex-direction': 'column'})

# Callback para actualizar el gráfico de barras
@app.callback(
    Output('bar_graph', 'figure'),
    [Input('radioitems', 'value')]
)
def update_bargraph(value):
    fig = px.bar(df, x='Gst ganado', y=value)
    return fig

# Callback para actualizar el gráfico de pastel
@app.callback(
    Output('pie_graph', 'figure'),
    [Input('radioitems', 'value')]
)
def update_piegraph(value):
    fig2 = px.pie(df, names='Gst ganado', values=value)
    return fig2

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)
