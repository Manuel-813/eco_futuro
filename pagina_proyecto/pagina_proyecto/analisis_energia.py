# Proyecto: ECO FUTURO - Análisis de Energía Renovable
# Bootcamp Talento Tec - Módulo de Programación Básica
# Autor: Karol Estupiñan Y Manuel Grajales
# Fecha: 24 de Octubre 2025

# IMPORTACIÓN DE LIBRERÍAS
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.offline import plot
import os


# 1. DEFINICIÓN DE RUTAS (AJUSTA ESTAS RUTAS SI ES NECESARIO)


# Ruta del archivo CSV (asegúrate de que sea correcta)
ruta_csv = "meta_FNCER.csv" 

# Carpeta donde guardarás los gráficos
carpeta_salida = "graficos_web" 

# Crear carpeta si no existe
os.makedirs(carpeta_salida, exist_ok=True)


# CARGA Y PREPARACIÓN DE DATOS


# Leer el CSV (usando separador ; y saltando líneas con errores)
df = pd.read_csv(ruta_csv, sep=";", encoding="utf-8", on_bad_lines="skip")

# Asegurar que la columna 'Capacidad' sea numérica y eliminar nulos
df['Capacidad'] = pd.to_numeric(df['Capacidad'], errors='coerce')
df = df.dropna(subset=['Tipo', 'Capacidad'])


# ANÁLISIS DESCRIPTIVO (SE MUESTRA EN LA CONSOLA)


print("======================================================")
print("              ANÁLISIS DESCRIPTIVO DE DATOS           ")
print("======================================================")

# Mostrar las primeras filas del DataFrame limpio
print("\n🔹 Vista previa de los datos limpios (head):")
print(df.head())

# Mostrar información general del DataFrame (tipos de datos, conteo de nulos)
print("\n🔹 Información general del DataFrame:")
print(df.info())

# Mostrar estadísticas descriptivas de la capacidad (mean, std, min, max, cuartiles)
print("\n🔹 Estadísticas descriptivas de la Capacidad (MW):")
print(df['Capacidad'].describe())

# Mostrar la capacidad total acumulada
capacidad_total = df['Capacidad'].sum()
print(f"\n🔹 Capacidad Total Acumulada: {capacidad_total:,.2f} MW")

# Mostrar el conteo de proyectos por tipo
print("\n🔹 Conteo de Proyectos por Tipo de Energía:")
print(df['Tipo'].value_counts())

print("======================================================")



# GENERACIÓN DE GRÁFICOS INTERACTIVOS (PLOTLY)


# Gráfico de barras: Capacidad Total por Tipo
fig_barras = px.bar(df.groupby('Tipo', as_index=False)['Capacidad'].sum(),
x='Tipo', y='Capacidad', color='Tipo',
title='Producción de Energía Renovable por Fuente (MW)')
plot(fig_barras, filename=os.path.join(carpeta_salida, 'grafico_barras.html'), auto_open=False)

# Gráfico de torta: Participación de Tipos
fig_torta = px.pie(df.groupby('Tipo', as_index=False)['Capacidad'].sum(),
names='Tipo', values='Capacidad',
title='Participación de Energías Renovables')
plot(fig_torta, filename=os.path.join(carpeta_salida, 'grafico_torta.html'), auto_open=False)

# Gráfico de líneas: Capacidad por Proyecto
fig_lineas = px.line(df.sort_values(by='Capacidad'),
x='Proyecto', y='Capacidad', color='Tipo',
title='Distribución de Capacidad Instalada por Proyecto')
plot(fig_lineas, filename=os.path.join(carpeta_salida, 'grafico_lineas.html'), auto_open=False)

# Gráfico de área: Comparación Apilada
fig_area = go.Figure()
for tipo in df['Tipo'].unique():
    data = df[df['Tipo'] == tipo]
fig_area.add_trace(go.Scatter(
x=data['Proyecto'],
y=data['Capacidad'],
mode='lines',
stackgroup='one',
name=tipo))
fig_area.update_layout(title='Comparación entre tipos de Energía Renovable (MW)')
plot(fig_area, filename=os.path.join(carpeta_salida, 'grafico_area.html'), auto_open=False)

print("\n✅ Todos los gráficos interactivos fueron creados correctamente en:")
print(carpeta_salida)