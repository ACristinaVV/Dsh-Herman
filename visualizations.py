import plotly.express as px
from data import sales

# Daily Sales Chart ---------------------------------------
chart = px.line(sales, x=sales.index, y="Total") # Grafica de lineas
# Str con subtitulo
subtitle = f"Ventas Diarias Promedio: {round(sales.iloc[:, 0].mean(), 2)}"
# Cambbiar titulo y Formato
chart.update_layout(title =f"Herman - Ventas Diarias  <br><sup>{subtitle}</sup>", title_x=0.5)
chart.update_traces(line_color='Black')
chart.show()