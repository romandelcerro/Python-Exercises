class Rectangulo:
    def __init__(self, largo, ancho):
            self.largo = largo
            self.ancho = ancho

    def area(self):
        return self.largo * self.ancho

    def perimetro(self):
        return 2 * (self.largo + self.ancho)

    def hov(self):
        if self.largo > self.ancho:
            return "Horizontal"
        else:
            return "Vertical"

    def dimensiones(self):
        print("Largo: {} \nAncho: {}".format(self.largo,self.ancho))

rect =Rectangulo(2,5)
print("Area: {}".format(rect.area()))
print("Perimetro: {}".format(rect.perimetro()))
print("Orientacion: {}".format(rect.hov()))

