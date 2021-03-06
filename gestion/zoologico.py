class Zoologico:
    def __init__(self, nombre, ubicacion, zona=False):
        self._nombre = nombre
        self._ubicacion = ubicacion
        self._zona = [] if not zona else zona

    def agregarZonas(self, zona):
        self._zona.append(zona)

    def cantidadTotalAnimales(self):
        t = 0
        for zona in self.getZona():
            t += zona.cantidadAnimales()
        return t

    def getNombre(self):
        return self._nombre
    def setNombre(self, nombre):
        self._nombre = nombre

    def getUbicacion(self):
        return self._ubicacion
    def setUbicacion(self, ubicacion):
        self._ubicacion = ubicacion

    def getZona(self):
        return self._zona
    def setZona(self, zona):
        self._zona = zona
