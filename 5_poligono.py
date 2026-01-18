"""
 Crea una única función (importante que solo sea una) que sea capaz
 de calcular y retornar el área de un polígono.
  - La función recibirá por parámetro solo UN polígono a la vez.
  - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
  - Imprime el cálculo del área de un polígono de cada tipo.
"""
#region classes
class Poligono:
    def __init__(self, base: int, height: int):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height

class Triangle(Poligono):

    def area(self):
        return (self.base * self.height) / 2

class Rectangle(Poligono):
    def area(self):
        return self.base * self.height

class Square(Poligono):
    def __init__(self, side: int):
        super().__init__(side, side)
        self.side = side

    def area(self):
        return self.side * self.side

#endregion

def area(poligono: Poligono):
    """
    Calcula el área de un polígono
    :param poligono: llamada a la clase de polígono con sus respectivos lados.
    :return: El área del polígono
    """
    return poligono.area()

if __name__ == "__main__":
    print(area(Triangle(2,3)))
    print(area(Rectangle(2,3)))
    print(area(Square(3)))