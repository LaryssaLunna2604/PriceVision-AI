from sklearn.linear_model import LinearRegression
import numpy as np

def treinar_modelo():
    x = np.array([10, 20, 30, 40, 50]).reshape(-1, 1)
    y = np.array([100, 200, 300, 400, 500])

    modelo = LinearRegression()
    modelo.fit(x, y)
    return modelo

def prever_preco(modelo, valor):
    return modelo.predict([[valor]])[0]
