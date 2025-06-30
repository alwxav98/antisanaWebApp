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

@app.route('/analisis')
def analisis():
    return render_template('analisis.html')

@app.route('/api/zona_sensores')
def zona_sensores():
    coords = manager.zona_envolvente()

    geojson = {
        "type": "Feature",
        "geometry": {
            "type": "Polygon",
            "coordinates": [[ [lon, lat] for lat, lon in coords ]]  # invertimos lat/lon
        },
        "properties": {
            "nombre": "Zona de cobertura de sensores"
        }
    }
    return jsonify(geojson)

@app.route('/dashboard')
def dashboard():
    sensores = manager.todos_dict()
    zonas = {
        "Reserva Ecológica Antisana": [],
        "Laguna La Mica": [],
        "Río Antisana": []
    }

    # Función simple para calcular distancia aproximada en km
    from math import radians, cos, sin, sqrt, atan2
    def distancia_km(lat1, lon1, lat2, lon2):
        R = 6371
        dlat = radians(lat2 - lat1)
        dlon = radians(lon2 - lon1)
        a = sin(dlat/2)**2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon/2)**2
        return R * (2 * atan2(sqrt(a), sqrt(1 - a)))

    # Clasificar sensores según cercanía
    for s in sensores:
        if distancia_km(s['latitud'], s['longitud'], -0.55, -78.25) < 7:
            zonas["Reserva Ecológica Antisana"].append(s)
        if distancia_km(s['latitud'], s['longitud'], -0.60, -78.20) < 2:
            zonas["Laguna La Mica"].append(s)
        if distancia_km(s['latitud'], s['longitud'], -0.54, -78.22) < 3:
            zonas["Río Antisana"].append(s)

    return render_template('dashboard.html', zonas=zonas)


@app.route('/visualizacion')
def visualizacion():
    import pandas as pd

    def cargar_y_filtrar(ruta):
        df = pd.read_csv(ruta)
        df.columns = df.columns.str.lower()
        # Eliminar filas con NaN
        df = df.dropna(subset=['valor'])
        return df[['fecha', 'valor']].to_dict(orient='records')

    data = {
        'P42': cargar_y_filtrar('data/P42-Antisana_Ramón_Huañuna_Precipitación-Diario.csv'),
        'P43': cargar_y_filtrar('data/P43-Antisana_Limboasi_Precipitación-Diario.csv'),
        'P55': cargar_y_filtrar('data/P55-Antisana_Diguchi_Precipitación-Diario.csv'),
    }

    return render_template('visualizacion.html', data=data)



if __name__ == '__main__':
    app.run(debug=True)
