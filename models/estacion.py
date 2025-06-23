class Sensor:
    def __init__(self, codigo, nombre, tipo, latitud, longitud, variable):
        self.codigo = codigo
        self.nombre = nombre
        self.tipo = tipo
        self.latitud = latitud
        self.longitud = longitud
        self.variable = variable

    def to_dict(self):
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "tipo": self.tipo,
            "latitud": self.latitud,
            "longitud": self.longitud,
            "variable": self.variable
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
