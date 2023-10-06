import pandas as pd
import plotly.graph_objs as go

# Importar la data
df = pd.read_csv('Dash/Corridas-Stepn-PowerbiS.csv')


def explorar_datos(df):
    # Grafico minado
    total_gst_ganado = df['Gst ganado'].sum()
    total_gmt = df['GMT'].fillna(0).sum()
    return total_gst_ganado, total_gmt  # Devuelve los resultados como una tupla
    



def calcular_totales_gst(df):
    # Grafico quema GST
    total_gst_para_cajas = df['Coste de caja gst'].sum()
    total_gst_para_reparaciones = df['Arreglo Gst'].sum()
    return total_gst_para_cajas,total_gst_para_reparaciones,
#     print(f'Total Coste de caja gst: {total_gst_para_cajas}')
#     print(f'Total Arreglo Gst: {total_gst_para_reparaciones}')

# # Llamamos a la función para calcular los totales GST
# calcular_totales_gst(df)

def calcular_gemas_lv(df, columna, valor_yes, valor_no, extra):
    conteo = df[columna].value_counts()
    cantidad_yes = int(conteo.get(valor_yes, 0))
    cantidad_no = int(conteo.get(valor_no, 0))
    total_gemas = (cantidad_yes + cantidad_no) * 3 + extra
    return total_gemas
#     print(f'Cantidad de "{valor_yes}" en {columna}: {cantidad_yes}')
#     print(f'Cantidad de "{valor_no}" en {columna}: {cantidad_no}')
#     print(f'Total de gemas {columna}: {total_gemas}')

# # Llamamos a la función para calcular gemas para LV1
# calcular_gemas_lv(df, 'Success LV1', 'YES', 'NO', 456)


# Rate de gemas 


def calcular_total_gst_upgrades(df):
    total_gemas_lv1 = calcular_gemas_lv(df, 'Success LV1', 'YES', 'NO', 456)
    total_gemas_lv2 = calcular_gemas_lv(df, 'Success LV2', 'YES', 'NO', 171)
    total_gemas_lv3 = calcular_gemas_lv(df, 'Success LV3', 'YES', 'NO', 56)
    total_gemas_lv4 = calcular_gemas_lv(df, 'Success LV4', 'YES', 'NO', 0)

    total_gst_upgrades = (total_gemas_lv1 / 3 * 50) + (total_gemas_lv2 / 3 * 100) + (total_gemas_lv3 / 3 * 200) + (total_gemas_lv4 / 3 * 300)

    return total_gst_upgrades




def calcular_porcentajes(df, columna, valor_yes, valor_no):
    conteo = df[columna].value_counts()
    cantidad_yes = int(conteo.get(valor_yes, 0))
    cantidad_no = int(conteo.get(valor_no, 0))
    
    if cantidad_yes + cantidad_no == 0:
        porcentaje_positivo = 0
        porcentaje_negativo = 0
        porcentaje_total = 0
    else:
        porcentaje_positivo = (cantidad_yes / (cantidad_yes + cantidad_no)) * 100
        porcentaje_negativo = 100 - porcentaje_positivo
        porcentaje_total = 100
        
    return porcentaje_positivo, porcentaje_negativo, porcentaje_total

porcentaje_positivo, porcentaje_negativo, porcentaje_total = calcular_porcentajes(df, 'Success LV1', 'YES', 'NO')

# print("Porcentaje Positivo:", porcentaje_positivo)
# print("Porcentaje Negativo:", porcentaje_negativo)
# print("Porcentaje Total:", porcentaje_total)





def procesar_cajas(df):
    # Filtrar filas donde 'Caja mb' no sea igual a 'F' y no sea NaN
    df_filtrado = df[(df['Caja mb'] != 'F') & (df['Caja mb'].notna())]
    
    # Convertir los valores restantes en 'Caja mb' a enteros
    df_filtrado.loc[:, 'Caja mb'] = df_filtrado['Caja mb'].astype(int)

    # Crear listas separadas para cada valor
    valores_3 = df_filtrado[df_filtrado['Caja mb'] == 3]['Caja mb'].tolist()
    valores_4 = df_filtrado[df_filtrado['Caja mb'] == 4]['Caja mb'].tolist()
    valores_5 = df_filtrado[df_filtrado['Caja mb'] == 5]['Caja mb'].tolist()
    valores_6 = df_filtrado[df_filtrado['Caja mb'] == 6]['Caja mb'].tolist()
    valores_7 = df_filtrado[df_filtrado['Caja mb'] == 7]['Caja mb'].tolist()
    valores_8 = df_filtrado[df_filtrado['Caja mb'] == 8]['Caja mb'].tolist()
    valores_9 = df_filtrado[df_filtrado['Caja mb'] == 9]['Caja mb'].tolist()
    valores_10 = df_filtrado[df_filtrado['Caja mb'] == 10]['Caja mb'].tolist()
    
    return {
        3: valores_3,
        4: valores_4,
        5: valores_5,
        6: valores_6,
        7: valores_7,
        8: valores_8,
        9: valores_9,
        10: valores_10
    }
# # # Ejemplo de uso
# resultados = procesar_cajas(df) #entrega listas
# print(len(resultados[4]))


def contar_ocurrencias(valores_dict):
    total_ocurrencias = sum(len(lista) for lista in valores_dict.values())
    return total_ocurrencias
# resultados = procesar_cajas(df)
# total_ocurrencias = contar_ocurrencias(resultados)
# print(total_ocurrencias)




def calcular_gemaseachcolor_lvYES(df, column_name, value_yes, value_no, num):
    # Inicializar diccionarios para YES y NO
    diccionario_eachcolor_NO = {'R': 0, 'C': 0, 'E': 0, 'L': 0}
    diccionario_eachcolor_YES = {'R': 0, 'C': 0, 'E': 0, 'L': 0}
    
    # Recorrer el DataFrame
    for index, row in df.iterrows():
        upgrades = row['Aclaraciones de Upgrades']
        
        # Verificar si el valor en 'Aclaraciones de Upgrades' es un str
        if isinstance(upgrades, str):
            # Extraer el nivel (level) y el color (color) de 'Aclaraciones de Upgrades'
            import re
            matches = re.findall(r'3([CERL]+)lv(\d+)', upgrades)
            
            for color, level in matches:
                if row[column_name] == value_yes:
                    diccionario_eachcolor_YES[color] += 1
                elif row[column_name] == value_no:
                    diccionario_eachcolor_NO[color] += 1
    
    return diccionario_eachcolor_YES, diccionario_eachcolor_NO

# # Ejemplo de uso:
# diccionario_eachcolor_YESLV3, diccionario_eachcolor_NOLV3 = calcular_gemaseachcolor_lvYES(df, 'Success LV3', 'YES', 'NO', 56)
# print("YES LV3:", diccionario_eachcolor_YESLV3)
# print("NO LV3:", diccionario_eachcolor_NOLV3)


