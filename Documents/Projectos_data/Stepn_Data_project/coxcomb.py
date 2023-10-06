import plotly.graph_objs as go
import pandas as pd
from datalimpia import *


diccionario_eachcolor_YESLV1, diccionario_eachcolor_NOLV1 = calcular_gemaseachcolor_lvYES(df, 'Success LV1', 'YES', 'NO', 456)

diccionario_eachcolor_YESLV2, diccionario_eachcolor_NOLV2= calcular_gemaseachcolor_lvYES(df, 'Success LV2', 'YES','NO', '171')

diccionario_eachcolor_YESLV3, diccionario_eachcolor_NOLV3 = calcular_gemaseachcolor_lvYES(df, 'Success LV3', 'YES', 'NO', 56)

diccionario_eachcolor_YESLV4, diccionario_eachcolor_NOLV4= calcular_gemaseachcolor_lvYES(df, 'Success LV4', 'YES', 'NO', 0)






# Datos de ejemplo para LV1
lv1_colors = ['C', 'E', 'L', 'R']
lv1_values = {
    'C': diccionario_eachcolor_YESLV1['C'],
    'E': diccionario_eachcolor_YESLV1['E'],
    'L': diccionario_eachcolor_YESLV1['L'],
    'R': diccionario_eachcolor_YESLV1['R']
}

# Datos de ejemplo para LV2
lv2_colors = ['C', 'E', 'L', 'R']
lv2_values = {
    'C': diccionario_eachcolor_YESLV2['C'],
    'E': diccionario_eachcolor_YESLV2['E'],
    'L': diccionario_eachcolor_YESLV2['L'],
    'R': diccionario_eachcolor_YESLV2['R']
}

# Define la función generate_coxcomb_chart para crear gráficos Coxcomb
def generate_coxcomb_chart(data_dict, level):
    colors = list(data_dict.keys())
    values = list(data_dict.values())

    fig = go.Figure(go.Barpolar(
        r=values,
        theta=colors,
        name=level,
        marker_color='blue'
    ))

    fig.update_layout(
        title=f'Coxcomb Chart {level}',
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, max(values)],
            )
        )
    )

    return fig


figurelv1 = generate_coxcomb_chart(lv1_values, 'LV1') 

figurelv2 = generate_coxcomb_chart(lv2_values, 'LV2') 


print(figurelv1)
print(figurelv2)