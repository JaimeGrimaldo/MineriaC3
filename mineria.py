# .:: SE TRABAJO EN 2 ALGORITMOS QUE SON CAPACES DE DETECTAR PRECIOS, EL 2DO ES MODIFICABLE A MAS DIAS ::.

# Jaime Eduardo Grimaldo Moreno - 191214 - 9no A
import mysql.connector as connection

mydb = connection.connect(
    host="database-1.cne0jl3cgfsu.us-east-1.rds.amazonaws.com",
    user="user-2",
    passwd="12345678",
    db="transactions"
)

query = "Select * from transactions;"
dataFrame = pd.read_sql(query, mydb)

dataframe.head()

p = Prophet(interval_width=0.92, daily_seasonality=True)
model = p.fit(dataframe)

future = p.make_future_dataframe(periods=365, freq='D')
future.tail()

forecast_prediction = p.predict(future)
forecast_prediction.tail()

plot1 = p.plot(forecast_prediction)

plot2 = p.plot_components(forecast_prediction)

# ======================================================================00

import numpy as np
import matplotlib.pyplot as plt

x=np.array([1,2,3,4,5])
y=np.array([11,12,13,14,15])

dia = 15
coeficiente = np.polyfit(x,y,2)
p= np.polyval(coeficiente, dia)

print("Precio:", dia, coeficiente)