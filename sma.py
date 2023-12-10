import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

# Definir el símbolo de la acción
ticker_symbol = "CLSK"  # Cambia AAPL por el símbolo de la acción que desees analizar

# Calcular las fechas hace dos años y la fecha actual
end_date = datetime.today().strftime('%Y-%m-%d')
start_date = (datetime.today() - timedelta(days=100)).strftime('%Y-%m-%d')  # 730 días equivalen a dos años

# Descargar los datos históricos de la acción
data = yf.download(ticker_symbol, start=start_date, end=end_date)

# Calcular la media móvil de 5 días
dias  = 5
data['SMA_' + str(dias)] = data['Close'].rolling(window=dias).mean()

dias  = 15
data['SMA_' + str(dias)] = data['Close'].rolling(window=dias).mean()


dias  = 30
data['SMA_' + str(dias)] = data['Close'].rolling(window=dias).mean()



data['Recomendacion'] = 'Esperar'  # Valor predeterminado de "Esperar"

# Calcular la diferencia entre las medias móviles
data['Diferencia'] = (data['SMA_5'] / data['SMA_30' ]) - 1

# Si la diferencia es mayor al 5%, se recomienda "Compra"
data.loc[data['Diferencia'] > 0.03, 'Recomendacion'] = 'Compra'

# Si la diferencia es menor al -5%, se recomienda "Venta"
data.loc[data['Diferencia'] < -0.03, 'Recomendacion'] = 'Venta'

# Mostrar los primeros registros de los datos
print(data.tail(20))

# Guardar los datos en un archivo Excel (.xlsx)
excel_filename = ticker_symbol + "_historico_precios4.xlsx"
data.to_excel(excel_filename)

print(f"Los datos se han guardado en el archivo: {excel_filename}")
