from shapely.geometry import MultiPoint
class Sensor:
    def __init__(self, codigo, nombre, tipo, latitud, longitud, variable,
                 contexto_geoambiental=None, reserva=None, fuente_hidrica=None,
                 ecosistema=None, influencia=None):
        self.codigo = codigo
        self.nombre = nombre
        self.tipo = tipo
        self.latitud = latitud
        self.longitud = longitud
        self.variable = variable
        self.contexto_geoambiental = contexto_geoambiental
        self.reserva = reserva
        self.fuente_hidrica = fuente_hidrica
        self.ecosistema = ecosistema
        self.influencia = influencia

    def to_dict(self):
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "tipo": self.tipo,
            "latitud": self.latitud,
            "longitud": self.longitud,
            "variable": self.variable,
            "contexto_geoambiental": self.contexto_geoambiental,
            "reserva": self.reserva,
            "fuente_hidrica": self.fuente_hidrica,
            "ecosistema": self.ecosistema,
            "influencia": self.influencia
        }



class EstacionManager:
    def __init__(self, sensores=None):
        self.sensores = sensores or []

    def cargar_desde_json(self, ruta):
        import json
        with open(ruta, 'r', encoding='utf-8') as f:
            datos = json.load(f)
        self.sensores = [Sensor(**s) for s in datos]

    def por_variable(self, variable):
        return [s for s in self.sensores if s.variable.lower() == variable.lower()]

    def todos_dict(self):
        return [s.to_dict() for s in self.sensores]

    def zona_envolvente(self):
        puntos = [(s.latitud, s.longitud) for s in self.sensores]
        multipunto = MultiPoint(puntos)
        poligono = multipunto.convex_hull
        return list(poligono.exterior.coords)
