import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Leer datos desde el archivo CSV
df = pd.read_csv('electronica_ventas.csv')

# Asegurar que la columna Fecha sea de tipo datetime
df['Fecha'] = pd.to_datetime(df['Fecha'], errors='coerce')

# Verificar si hay valores nulos después de la conversión
if df['Fecha'].isnull().sum() > 0:
    print("Hay valores nulos en la columna 'Fecha' después de la conversión.")
    print(df[df['Fecha'].isnull()])

# Calcular ingresos (Ventas * Precio)
df['Ingresos'] = df['Ventas'] * df['Precio']

# Crear la columna 'Mes'
df['Mes'] = df['Fecha'].dt.month

# Verificar que la columna 'Mes' se ha creado correctamente
print(df[['Fecha', 'Mes']].head())

# Análisis descriptivo
print("Estadísticas descriptivas del dataset:")
print(df.describe())

# Detección de valores atípicos (Outliers)
q1 = df['Ventas'].quantile(0.25)
q3 = df['Ventas'].quantile(0.75)
iqr = q3 - q1
outliers = df[(df['Ventas'] < (q1 - 1.5 * iqr)) | (df['Ventas'] > (q3 + 1.5 * iqr))]
print("\nValores atípicos en Ventas:")
print(outliers)

# Análisis adicional

# 1. Análisis de la Distribución de Precios
plt.figure(figsize=(8, 6))
plt.hist(df['Precio'], bins=20, color='purple', edgecolor='black')
plt.title('Distribución de Precios')
plt.xlabel('Precio')
plt.ylabel('Frecuencia')
plt.grid()
plt.show()

# 2. Relación entre Ventas e Ingresos
plt.figure(figsize=(8, 6))
plt.scatter(df['Ventas'], df['Ingresos'], alpha=0.5)
plt.title('Relación entre Ventas e Ingresos')
plt.xlabel('Ventas')
plt.ylabel('Ingresos')
plt.grid()
plt.show()

# 3. Ventas por Año
df['Año'] = df['Fecha'].dt.year
ventas_anuales = df.groupby('Año')['Ventas'].sum()
plt.figure(figsize=(8, 6))
ventas_anuales.plot(kind='bar', title='Ventas por Año')
plt.ylabel('Ventas')
plt.xlabel('Año')
plt.grid()
plt.show()

# 4. Promedio de Precios por Producto
promedio_precio_producto = df.groupby('Producto')['Precio'].mean()
plt.figure(figsize=(8, 6))
promedio_precio_producto.plot(kind='bar', color='green', title='Promedio de Precios por Producto')
plt.ylabel('Precio Promedio')
plt.grid()
plt.show()

# 5. Ventas por Categoría (si la columna existe)
if 'Categoría' in df.columns:
    ventas_categoria = df.groupby('Categoría')['Ventas'].sum()
    plt.figure(figsize=(8, 6))
    ventas_categoria.plot(kind='bar', color='blue', title='Ventas por Categoría')
    plt.ylabel('Ventas')
    plt.grid()
    plt.show()

# 6. Evolución Mensual de Ingresos
ingresos_mensuales = df.groupby('Mes')['Ingresos'].sum()
plt.figure(figsize=(8, 6))
ingresos_mensuales.plot(kind='line', marker='o', color='red', title='Evolución Mensual de Ingresos')
plt.ylabel('Ingresos')
plt.xlabel('Mes')
plt.grid()
plt.show()

# 7. Análisis de Desviación Estándar de Ventas por Región
std_ventas_region = df.groupby('Region')['Ventas'].std()
plt.figure(figsize=(8, 6))
std_ventas_region.plot(kind='bar', color='cyan', title='Desviación Estándar de Ventas por Región')
plt.ylabel('Desviación Estándar')
plt.grid()
plt.show()

# 8. Mapa de Calor de la Correlación de Todas las Variables Numéricas
plt.figure(figsize=(10, 8))
numerical_df = df.select_dtypes(include=[np.number])
sns.heatmap(numerical_df.corr(), annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Mapa de Calor de Correlación')
plt.show()



