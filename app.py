from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Renderiza el archivo index.html en la ruta principal
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Configura para escuchar en el puerto 5000
    