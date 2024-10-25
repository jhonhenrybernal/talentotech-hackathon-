from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
from base64 import b64encode
from prophet import Prophet
import json

app = Flask(__name__)
CORS(app)  # Habilita CORS para toda la aplicación

# Cargar datos del archivo JSON
with open('M4_DataTecnologia.json') as f:
    data = json.load(f)

# Ruta para la página principal (index.html)
@app.route('/')
def home():
    return render_template('about.html')

@app.route('/index')
def home():
    return render_template('index.html')


@app.route('/home')
def predicciones():
    return render_template('home.html')

# Función para generar predicciones usando Prophet
def generar_prediccion(sector):
    # Filtrar datos según el sector
    datos_sector = [d for d in data if d['Sector'] == sector]
    if not datos_sector:
        return None

    datos_sector = datos_sector[0]
    
    # Crear un DataFrame simulado para Prophet
    fechas = pd.date_range(start='2024-01-01', periods=12, freq='M')
    valores = np.random.rand(12) * 100  # Simulando valores
    df = pd.DataFrame({'ds': fechas, 'y': valores})

    # Usar Prophet para predicción
    modelo = Prophet()
    modelo.fit(df)
    futuro = modelo.make_future_dataframe(periods=6, freq='M')
    pronostico = modelo.predict(futuro)

    # Generar gráfica
    fig, ax = plt.subplots(figsize=(10, 6))
    modelo.plot(pronostico, ax=ax)
    plt.title(f"Predicción para el sector {sector}")
    
    # Guardar gráfica en memoria y codificar a base64
    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    grafico_base64 = b64encode(img.getvalue()).decode('utf-8')

    return grafico_base64

# Ruta para obtener predicción
@app.route('/prediccion', methods=['GET'])
def prediccion():
    sector = request.args.get('sector')
    if not sector:
        return jsonify({"error": "Sector no especificado"}), 400

    grafico = generar_prediccion(sector)
    if grafico is None:
        return jsonify({"error": "Sector no encontrado"}), 404
    
    return jsonify({"grafico": grafico})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
