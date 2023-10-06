
import plotly.graph_objs as go
import re
import pandas as pd
from datalimpia import *

#Carga de CSV
df = pd.read_csv('Dash/Corridas-Stepn-PowerbiS.csv')


# Variables y funciones
resultados_minado = explorar_datos(df)
gstquemados = calcular_totales_gst(df)
resultadocajas = procesar_cajas(df)
valores_dict= resultadocajas
total_ocurrencias = contar_ocurrencias(valores_dict)
total_gst_upgrades = calcular_total_gst_upgrades(df)


# Llamamos a la función para calcular gemas para LV1
total_gemas_lv1 = calcular_gemas_lv(df, 'Success LV1', 'YES', 'NO', 456)
# Llamamos a la función para calcular gemas para LV2
total_gemas_lv2 = calcular_gemas_lv(df, 'Success LV2', 'YES', 'NO', 171)
# Llamamos a la función para calcular gemas para LV3
total_gemas_lv3 = calcular_gemas_lv(df, 'Success LV3', 'YES', 'NO', 56)
# Llamamos a la función para calcular gemas para LV4
total_gemas_lv4 = calcular_gemas_lv(df, 'Success LV4', 'YES', 'NO', 0)


# Obtener el valor de cada caja por separado :
cajas_mb3 = (len(resultadocajas[3]))
cajas_mb4 = (len(resultadocajas[4]))
cajas_mb5 = (len(resultadocajas[5]))
cajas_mb6 = (len(resultadocajas[6]))
cajas_mb7 = (len(resultadocajas[7]))
cajas_mb8 = (len(resultadocajas[8]))
cajas_mb9 = (len(resultadocajas[9]))
cajas_mb10 = (len(resultadocajas[10]))


# Llamamos a la función para calcular rate gemas lv1
porcentaje_positivo_lv1, porcentaje_negativo_lv1, porcentaje_total_lv1 = calcular_porcentajes(df, 'Success LV1', 'YES', 'NO')

# Llamamos a la función para calcular rate gemas lv2
porcentaje_positivo_lv2, porcentaje_negativo_lv2, porcentaje_total_lv2 = calcular_porcentajes(df, 'Success LV2', 'YES', 'NO')

# Llamamos a la función para calcular rate gemas lv3
porcentaje_positivo_lv3, porcentaje_negativo_lv3, porcentaje_total_lv3 = calcular_porcentajes(df, 'Success LV3', 'YES', 'NO')

# Llamamos a la función para calcular rate gemas lv4
porcentaje_positivo_lv4, porcentaje_negativo_lv4, porcentaje_total_lv4 = calcular_porcentajes(df, 'Success LV4', 'YES', 'NO')


diccionario_eachcolor_YESLV1, diccionario_eachcolor_NOLV1 = calcular_gemaseachcolor_lvYES(df, 'Success LV1', 'YES', 'NO', 456)

diccionario_eachcolor_YESLV2, diccionario_eachcolor_NOLV2= calcular_gemaseachcolor_lvYES(df, 'Success LV2', 'YES','NO', '171')

diccionario_eachcolor_YESLV3, diccionario_eachcolor_NOLV3 = calcular_gemaseachcolor_lvYES(df, 'Success LV3', 'YES', 'NO', 56)

diccionario_eachcolor_YESLV4, diccionario_eachcolor_NOLV4= calcular_gemaseachcolor_lvYES(df, 'Success LV4', 'YES', 'NO', 0)

total_exitos_lv3 = sum(diccionario_eachcolor_YESLV3.values())

traces_minado = {
'gst mianed':go.Bar(
    x=['Total'], y=[resultados_minado[0]], name='$GST mained'),

'gmt mained': go.Bar(
    x=['Total'], y=[resultados_minado[1]], name='$GMT mained') 
}

traces_gstquemado = {
    'Gst_quemado_mb':go.Bar
                     (x=['Total'], y=[gstquemados[0]], name='Gst burned for mb'),

    'gst_repair_sneakers':go.Bar
    (x=['Total'], y=[gstquemados[1]], name='Gst burned for repair sneakers'),

    'gst_quemado_upgrades' :go.Bar
    (x=['Total'], y=[total_gst_upgrades], name='Gst burned for upgrades'),

    'totaldegstquemado': go.Bar
    (x=['Total'], y=[gstquemados[0]+gstquemados[1]+total_gst_upgrades], name='Gst burned')
}

traces_cajas = {
    'mb3': go.Bar(
        x=['mb 3'], y=[cajas_mb3], name='mb3 obteined'),

    'mb4': go.Bar(
        x=['mb 4'], y=[cajas_mb4], name='mb4 obteined'),

    'mb5': go.Bar(
        x=['mb 5'], y=[cajas_mb5], name='mb5 obteined'),

    'mb6': go.Bar(
        x=['mb 6'], y=[cajas_mb6], name='mb6 obteined'),

    'mb7': go.Bar(
        x=['mb 7'], y=[cajas_mb7], name='mb7 obteined'),

    'mb8': go.Bar(
        x=['mb 8'], y=[cajas_mb8], name='mb8 obteined'),

    'mb9': go.Bar(
        x=['mb 9'], y=[cajas_mb9], name='mb9 obteined'),

    'mb10': go.Bar(
        x=['mb 10'], y=[cajas_mb10], name='mb10 obteined'),

    'total mbs': go.Bar(
        x=['Total'], y=[total_ocurrencias], name='$Total MBS')
}

traces_gemall_combined = {
    'lv1': {
        'lv1gems_burned': go.Bar(x=['Total'], y=[total_gemas_lv1], name='lv1 gems burned'),
        'lv1gems_totalups': go.Bar(x=['Total'], y=[total_gemas_lv1 / 3], name='total ups lv1')
    },
    'lv2': {
        'lv2gems_burned': go.Bar(x=['Total'], y=[total_gemas_lv2], name='lv2 gems burned'),
        'lv2gems_totalups': go.Bar(x=['Total'], y=[total_gemas_lv2 / 3], name='total ups lv2')
    },
    'lv3': {
        'lv3gems_burned': go.Bar(x=['Total'], y=[total_gemas_lv3], name='lv3 gems burned'),
        'lv3gems_totalups': go.Bar(x=['Total'], y=[total_gemas_lv3 / 3], name='total ups lv3')
    },
    'lv4': {
        'lv4gems_burned': go.Bar(x=['Total'], y=[total_gemas_lv4], name='lv4 gems burned'),
        'lv4gems_totalups': go.Bar(x=['Total'], y=[total_gemas_lv4 / 3], name='total ups lv4')
    }
}

rate_gemstraces = {
    'lv1': go.Pie(
        labels=['Success', 'Fail'],
        values=[porcentaje_positivo_lv1, porcentaje_negativo_lv1],
        name='lv1 gems'
    ),
    'lv2': go.Pie(
        labels=['Success', 'Fail'],
        values=[porcentaje_positivo_lv2, porcentaje_negativo_lv2],
        name='lv2 gems'
    ),
    'lv3': go.Pie(
        labels=['Success', 'Fail'],
        values=[porcentaje_positivo_lv3, porcentaje_negativo_lv3],
        name='lv3 gems'
    ),
    'lv4': go.Pie(
        labels=['Success', 'Fail'],
        values=[porcentaje_positivo_lv4, porcentaje_negativo_lv4],
        name='lv4 gems'
    )
}

eachcolor_rate = {
    'lv1': go.Pie(
        labels=['C', 'E', 'L', 'R'],
        values=[
            ((diccionario_eachcolor_YESLV1['C']/ (diccionario_eachcolor_YESLV1['C'] + diccionario_eachcolor_NOLV1['C']) )),
           ((diccionario_eachcolor_YESLV1['E']/ (diccionario_eachcolor_YESLV1['E'] + diccionario_eachcolor_NOLV1['E']) )),
           ((diccionario_eachcolor_YESLV1['L']/ (diccionario_eachcolor_YESLV1['L'] + diccionario_eachcolor_NOLV1['L']) )),
           ((diccionario_eachcolor_YESLV1['R']/ (diccionario_eachcolor_YESLV1['R'] + diccionario_eachcolor_NOLV1['R']) )),
        ],
        title='Success Rate for LV1',
    ),
   'lv2': go.Pie(
        labels=['C', 'E', 'L', 'R'],
        values=[
            ((diccionario_eachcolor_YESLV2['C'] / (diccionario_eachcolor_YESLV2['C'] + diccionario_eachcolor_NOLV2['C']))),
            ((diccionario_eachcolor_YESLV2['E'] / (diccionario_eachcolor_YESLV2['E'] + diccionario_eachcolor_NOLV2['E']))),
            ((diccionario_eachcolor_YESLV2['L'] / (diccionario_eachcolor_YESLV2['L'] + diccionario_eachcolor_NOLV2['L']))),
            ((diccionario_eachcolor_YESLV2['R'] / (diccionario_eachcolor_YESLV2['R'] + diccionario_eachcolor_NOLV2['R']))),
        ],
        title='Success Rate for LV2',
    ),
    'lv3': go.Pie(
    labels=['C', 'E', 'L', 'R'],
    values=[
        ((diccionario_eachcolor_YESLV3['C'] / (diccionario_eachcolor_YESLV3['C'] + diccionario_eachcolor_NOLV3['C']))),
        ((diccionario_eachcolor_YESLV3['E'] / (diccionario_eachcolor_YESLV3['E'] + diccionario_eachcolor_NOLV3['E']))),
        ((diccionario_eachcolor_YESLV3['L'] / (diccionario_eachcolor_YESLV3['L'] + diccionario_eachcolor_NOLV3['L']))),
        ((diccionario_eachcolor_YESLV3['R'] / (diccionario_eachcolor_YESLV3['R'] + diccionario_eachcolor_NOLV3['R']))),
    ],
    title='Success Rate for LV3',
    ),
    'lv4': go.Pie(
        labels=['L', 'R'],
        values=[
            ((diccionario_eachcolor_YESLV4['L'] / (diccionario_eachcolor_YESLV4['L'] + diccionario_eachcolor_NOLV4['L']))),
            ((diccionario_eachcolor_YESLV4['R'] / (diccionario_eachcolor_YESLV4['R'] + diccionario_eachcolor_NOLV4['R']))),
        ],
        title='Success Rate for LV4',
    ),
    }

