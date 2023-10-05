import dash
from dash import dcc, html
import plotly.graph_objs as go
import pandas as pd
from datalimpia import explorar_datos, calcular_totales_gst, calcular_gemas_lv,procesar_cajas, contar_ocurrencias, calcular_porcentajes


df = pd.read_csv('Dash/Corridas-Stepn-PowerbiS.csv')
resultados_minado = explorar_datos(df)
gstquemados = calcular_totales_gst(df)
resultadocajas = procesar_cajas(df)
valores_dict= resultadocajas
total_ocurrencias = contar_ocurrencias(valores_dict)


# Obtener el valor de cada caja por separado :
cajas_mb3 = (len(resultadocajas[3]))
cajas_mb4 = (len(resultadocajas[4]))
cajas_mb5 = (len(resultadocajas[5]))
cajas_mb6 = (len(resultadocajas[6]))
cajas_mb7 = (len(resultadocajas[7]))
cajas_mb8 = (len(resultadocajas[8]))
cajas_mb9 = (len(resultadocajas[9]))
cajas_mb10 = (len(resultadocajas[10]))


# Llamamos a la función para calcular gemas para LV1
total_gemas_lv1 = calcular_gemas_lv(df, 'Success LV1', 'YES', 'NO', 456)
# Llamamos a la función para calcular gemas para LV2
total_gemas_lv2 = calcular_gemas_lv(df, 'Success LV2', 'YES', 'NO', 171)
# Llamamos a la función para calcular gemas para LV3
total_gemas_lv3 = calcular_gemas_lv(df, 'Success LV3', 'YES', 'NO', 56)
# Llamamos a la función para calcular gemas para LV4
total_gemas_lv4 = calcular_gemas_lv(df, 'Success LV4', 'YES', 'NO', 0)

total_gst_upgrades = (total_gemas_lv1 / 3 * 50) + (total_gemas_lv2 / 3 * 100) + (total_gemas_lv3 / 3 * 200) + (total_gemas_lv4 / 3 * 300)


# Llamamos a la función para calcular rate gemas lv1
porcentaje_positivo_lv1, porcentaje_negativo_lv1, porcentaje_total_lv1 = calcular_porcentajes(df, 'Success LV1', 'YES', 'NO')

# Llamamos a la función para calcular rate gemas lv2
porcentaje_positivo_lv2, porcentaje_negativo_lv2, porcentaje_total_lv2 = calcular_porcentajes(df, 'Success LV2', 'YES', 'NO')

# Llamamos a la función para calcular rate gemas lv3
porcentaje_positivo_lv3, porcentaje_negativo_lv3, porcentaje_total_lv3 = calcular_porcentajes(df, 'Success LV3', 'YES', 'NO')

# Llamamos a la función para calcular rate gemas lv4
porcentaje_positivo_lv4, porcentaje_negativo_lv4, porcentaje_total_lv4 = calcular_porcentajes(df, 'Success LV4', 'YES', 'NO')


# TRACE:

# Grafico minado
trace1 = go.Bar(x=['Total'], y=[resultados_minado[0]], name='$GST mained')
trace2 = go.Bar(x=['Total'], y=[resultados_minado[1]], name='$GMT mained')

# Grafico mbs minadas
# Crear el gráfico de barras en Plotly
trace11 = go.Bar(x=['mb 3'], y=[cajas_mb3], name='mb3 obteined')
trace12 = go.Bar(x=['mb 4'], y=[cajas_mb4], name='mb4 obteined')
trace13 = go.Bar(x=['mb 5'], y=[cajas_mb5], name='mb5 obteined')
trace14 = go.Bar(x=['mb 6'], y=[cajas_mb6], name='mb6 obteined')
trace15 = go.Bar(x=['mb 7'], y=[cajas_mb7], name='mb7 obteined')
trace16 = go.Bar(x=['mb 8'], y=[cajas_mb8], name='mb8 obteined')
trace17 = go.Bar(x=['mb 9'], y=[cajas_mb9], name='mb9 obteined')
trace18 = go.Bar(x=['mb 10'], y=[cajas_mb10], name='mb10 obteined')
trace19 = go.Bar(x=['Total'], y=[total_ocurrencias], name='$Total MBS')


# Grafico quema GST
trace3 = go.Bar(x=['Total'], y=[gstquemados[0]], name='Gst burned for mb')
trace4 = go.Bar(x=['Total'], y=[gstquemados[1]], name='Gst burned for repair sneakers')
trace9 = go.Bar(x=['Total'], y=[total_gst_upgrades], name='Gst burned for upgrades')
# tracetotal = go.Bar(x=['Total'], y=[gstquemadostotales], name='Gst burned')

trace5 = go.Bar(x=['Total'], y=[total_gemas_lv1], name='lv1 gems burned')
trace24 = go.Bar(x=['Total'], y=[total_gemas_lv1 / 3], name='total ups lv1')

trace6 = go.Bar(x=['Total'], y=[total_gemas_lv2], name='lv2 gems burned')
trace25 = go.Bar(x=['Total'], y=[total_gemas_lv2 / 3], name='total ups lv2')

trace7 = go.Bar(x=['Total'], y=[total_gemas_lv3], name='lv3 gems burned')
trace26 = go.Bar(x=['Total'], y=[total_gemas_lv3 / 3], name='total ups lv3')

trace8 = go.Bar(x=['Total'], y=[total_gemas_lv4], name='lv4 gems burned')
trace27 = go.Bar(x=['Total'], y=[total_gemas_lv4 / 3], name='total ups lv4')



# Grafico porcentaje rate total de gemas :

trace20 = go.Pie(labels=['Positivo', 'Negativo'], 
                 values=[porcentaje_positivo_lv1, porcentaje_negativo_lv1], 
                 name='lv1 gems')

trace21 = go.Pie(labels=['Positivo', 'Negativo'], 
                 values=[porcentaje_positivo_lv2, porcentaje_negativo_lv2], 
                 name='lv2 gems')

trace22 = go.Pie(labels=['Positivo', 'Negativo'], 
                 values=[porcentaje_positivo_lv3, porcentaje_negativo_lv3], 
                 name='lv3 gems')

trace23 = go.Pie(labels=['Positivo', 'Negativo'], 
                 values=[porcentaje_positivo_lv4, porcentaje_negativo_lv4], 
                 name='lv4 gems')



# Grafico porcentaje rate por color de gemas y por color




app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='Dashboard by @Mortadelamata'),
    html.Div(children='''This is my personal data for my runs, collaborate with me, DM me on Twitter'''),
    dcc.Graph(
        id='Graph-mined-assets',
        figure={
            'data': [trace1, trace2],
            'layout': go.Layout(title='500 days minning assets of stepn graph', barmode='group')
        }),

    dcc.Graph(
        id='Graph-Mb-Mined graph',
        figure={
            'data': [trace11,trace12,trace13,trace14,trace15,trace16,trace17,trace18,trace19],
            'layout': go.Layout(title='500 days of searching mbs graph', barmode='group')
        }),

    dcc.Graph(
        id='Graph-burned-gst for',
        figure={
            'data': [trace3, trace4, trace9],
            'layout': go.Layout(title='500 days burning gst graph', barmode='group')
        }),

    dcc.Graph(
        id='combined-graph',
        figure={
            'data': [trace5,trace24, trace6, trace25, trace7, trace26, trace8, trace27],
            'layout': go.Layout(title='Gems upgraded by me in 500 days', barmode='group')
        }
    ),
    dcc.Graph(
        id='pie-chartlv1',
        figure={
            'data': [trace20],
            'layout': go.Layout(title='Rate gems for levels by me in 500 days', barmode='group')
        }
    ),
    dcc.Graph(
        id='pie-chartlv2',
        figure={
            'data': [trace21],
            'layout': go.Layout(title='Rate gems for levels by me in 500 days', barmode='group')
        }
    ),
    dcc.Graph(
        id='pie-chartlv3',
        figure={
            'data': [trace22],
            'layout': go.Layout(title='Rate gems for levels by me in 500 days', barmode='group')
        }
    ),
    dcc.Graph(
        id='pie-chartlv4',
        figure={
            'data': [trace23],
            'layout': go.Layout(title='Rate gems for levels by me in 500 days', barmode='group')
        }
    ),
])


if __name__ == '__main__':
    app.run_server(debug=True)


