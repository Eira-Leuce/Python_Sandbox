class Vector:
    __type = "Vector"

    def __init__(self, xcord, ycord):
        self.__xcord = xcord
        self.__ycord = ycord
        print(f"Создан вектор с координатами [{self.__xcord}, {self.__ycord}]")

    @property
    def coordinates(self):
        print(f"Координаты вектора: x = [{self.__xcord}], y = [{self.__ycord}]")
        return (self.__xcord, self.__ycord)

    @coordinates.setter
    def coordinates(self, value):
        self.__xcord, self.__ycord = value
        print("Координаты были изменены")

    def __add__(self, other):
        return Vector(self.__xcord + other.__xcord, self.__ycord + other.__ycord)

    def __sub__(self, other):
        return Vector(self.__xcord - other.__xcord, self.__ycord - other.__ycord)


vector_a = Vector(2, 4)
vector_b = Vector(8, 5)
vector_a.coordinates
vector_b.coordinates
vector_c = vector_a + vector_b
vector_d = vector_a - vector_b
print(f"Координаты нового вектора: {vector_c.coordinates}")
print(f"Координаты нового вектора: {vector_d.coordinates}")