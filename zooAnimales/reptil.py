from zooAnimales.animal import Animal

class Reptil(Animal):
    listado = []
    serpientes = 0
    iguanas = 0
    def __init__(self, nombre, edad, habitat, genero, colorEscamas, largoCola):
        super().__init__(nombre, edad, habitat, genero)
        self._largoCola = largoCola
        self._colorEscamas = colorEscamas
        Reptil.listado.append(self)

    @staticmethod
    def cantidadReptiles():
        return len(Reptil.listado)

    def movimiento():
        return "reptar"

    @staticmethod
    def crearIguana(nombre, edad, genero):
        Reptil.iguanas += 1
        return Reptil(nombre, edad, "humedal", genero, "verde", 3)

    @staticmethod
    def crearSerpiente(nombre, edad, genero):
        Reptil.serpientes += 1
        return Reptil(nombre, edad, "jungla", genero, "blanco", 1)

    def getColorEscamas(self):
        return self._colorEscamas
    def setColorEscamas(self, colorEscamas):
        self._colorEscamas = colorEscamas

    def getLargoCola(self):
        return self._largoCola
    def setLargoCola(self, largoCola):
        self._largoCola = largoCola