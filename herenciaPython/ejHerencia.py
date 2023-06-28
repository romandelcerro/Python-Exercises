import math

class Figura:
    def __init__(self, color):
        self.color = color

    def area(self):
        pass

    def perimetro(self):
        pass

    def comparar(self, figura):
        return (type(self) == type(figura) and
                self.color == figura.color and
                self.calcular_area() == figura.calcular_area())

class Circulo(Figura):
    def __init__(self, color, radio):
        Figura.__init__(self,color)
        self.radio = radio

    def getRadio(self):
        return self.radio

    def setRadio(self,radio):
        self.radio = radio

    def area(self):
        return math.pi * pow(self.radio,2)

    def perimetro(self):
        return 2 * math.pi * self.radio

class Cuadrado(Figura):
    def __init__(self, color, lado):
        Figura.__init__(self,color)
        self.lado = lado

    def getLado(self):
        return self.lado

    def setLado(self,lado):
        self.lado = lado

    def area(self):
        return pow(self.lado,2)

    def perimetro(self):
        return 4 * self.lado

circulo = Circulo("Azul", 3)
cuadrado = Cuadrado("Verde",10)
print(circulo.perimetro())
print(circulo.area())
print(cuadrado.area())
print(cuadrado.perimetro())