import dash
from dash import dcc, html
import plotly.graph_objs as go
import pandas as pd
from Traces import rate_gemstraces, traces_minado, traces_cajas, traces_gstquemado, traces_gemall_combined

#Carga de CSV
df = pd.read_csv('Dash/Corridas-Stepn-PowerbiS.csv')



# Trace assets minado
minado_gst =traces_minado['gst mianed']
minado_gmt =traces_minado['gmt mained']

# Trace gst quemado
Gst_quemado_mb = traces_gstquemado['Gst_quemado_mb']
gst_repair_sneakers = traces_gstquemado['gst_repair_sneakers']
gst_quemado_upgrades = traces_gstquemado['gst_quemado_upgrades']
totaldegstquemado = traces_gstquemado['totaldegstquemado']

# Trace mbs minadas
trace_mb3 = traces_cajas['mb3']
trace_mb4 = traces_cajas['mb4']
trace_mb5 = traces_cajas['mb5']
trace_mb6 = traces_cajas['mb6']
trace_mb7 = traces_cajas['mb7']
trace_mb8 = traces_cajas['mb8']
trace_mb9 = traces_cajas['mb9']
trace_mb10 = traces_cajas['mb10']
trace_total_mbs = traces_cajas['total mbs']

# Trace quemas y ups de gemas todos los niveles disponibles

lv1gems_burned = traces_gemall_combined['lv1']['lv1gems_burned']
lv1gems_totalups = traces_gemall_combined['lv1']['lv1gems_totalups']

lv2gems_burned = traces_gemall_combined['lv2']['lv2gems_burned']
lv2gems_totalups = traces_gemall_combined['lv2']['lv2gems_totalups']

lv3gems_burned = traces_gemall_combined['lv3']['lv3gems_burned']
lv3gems_totalups = traces_gemall_combined['lv3']['lv3gems_totalups']

lv4gems_burned = traces_gemall_combined['lv4']['lv4gems_burned']
lv4gems_totalups = traces_gemall_combined['lv4']['lv4gems_totalups']


# Trace rate gems
trace_lv1 = rate_gemstraces['lv1']
trace_lv2 = rate_gemstraces['lv2']
trace_lv3 = rate_gemstraces['lv3']
trace_lv4 = rate_gemstraces['lv4']


app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='Dashboard by @Mortadelamata'),
    html.Div(children='''This is my personal data for my runs, collaborate with me, DM me on Twitter'''),

    dcc.Graph(
        id='Graph-mined-assets',
        figure={
            'data': [minado_gst, minado_gmt],
            'layout': go.Layout(title='500 days minning assets of stepn graph', barmode='group')
        }),

    dcc.Graph(
        id='Graph-Mb-Mined graph',
        figure={
            'data': [trace_mb3,trace_mb4,trace_mb5,trace_mb6,trace_mb7,trace_mb8,trace_mb9,trace_mb10,trace_total_mbs],
            'layout': go.Layout(title='500 days of searching mbs graph', barmode='group')
        }),

    dcc.Graph(
        id='Graph-burned-gst for',
        figure={
            'data': [Gst_quemado_mb, gst_repair_sneakers, gst_quemado_upgrades,totaldegstquemado],
            'layout': go.Layout(title='500 days burning gst graph', barmode='group')
        }),

    dcc.Graph(
        id='combined-graph',
        figure={
            'data': [lv1gems_burned, lv1gems_totalups,lv2gems_burned, lv2gems_totalups,lv3gems_burned, lv3gems_totalups,lv4gems_burned, lv4gems_totalups],
            'layout': go.Layout(title='Gems upgraded by me in 500 days', barmode='group')
        }
    ),


html.Div([
        dcc.Graph(
            id='pie-chartlv1',
            figure={
                'data': [trace_lv1],
                'layout': go.Layout(title={
                'text': f'Totals of ups in this chart are {lv1gems_totalups}',
                'font': {
                    'size': 12  # Tamaño de fuente deseado
                }
            }, barmode='group')
            },
            className='pie-chart'
        ),
        dcc.Graph(
            id='pie-chartlv2',
            figure={
                'data': [trace_lv2],
                'layout': go.Layout(title={
                'text': f'Totals of ups in this chart are {lv2gems_totalups}',
                'font': {
                    'size': 12  # Tamaño de fuente deseado
                }
            },
            barmode='group')
            },
            className='pie-chart'
        ),
        dcc.Graph(
            id='pie-chartlv3',
            figure={
                'data': [trace_lv3],
                'layout': go.Layout(title={
                'text': f'Totals of ups in this chart are {lv3gems_totalups}',
                'font': {
                    'size': 12  # Tamaño de fuente deseado
                }
            }, barmode='group')
            },
            className='pie-chart'
        ),
        dcc.Graph(
            id='pie-chartlv4',
            figure={
                'data': [trace_lv4],
                'layout': go.Layout(title={
                'text': f'Totals of ups in this chart are {lv4gems_totalups}',
                'font': {
                    'size': 12  # Tamaño de fuente deseado
                }
            }, barmode='group')
            },
            className='pie-chart'
        ),
    ]),  

])  

if __name__ == '__main__':
    app.run_server(debug=True)