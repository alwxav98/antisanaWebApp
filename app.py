from flask import Flask, render_template, jsonify
from models.estacion import EstacionManager

app = Flask(__name__)

manager = EstacionManager()
manager.cargar_desde_json('data/estaciones.json')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mapa')
def mapa():
    sensores = manager.todos_dict()
    return render_template('mapa.html', sensores=sensores)

@app.route('/api/estaciones')
def api_estaciones():
    return jsonify(manager.todos_dict())

if __name__ == '__main__':
    app.run(debug=True)
