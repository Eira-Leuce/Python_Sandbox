class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area(self):
        return self.width * self.length

    def perimeter(self):
        return 2 * self.width + 2 * self.length


abcd = Rectangle(2, 3)
efgh = Rectangle(4, 9)
ijkl = Rectangle(3, 14)

print("Площадь 1-го прямоугольника равна", abcd.area(),
      "\nПериметр 1-го прямоугольника равна", abcd.perimeter(),
      "\nПлощадь 2-го прямоугольника равна", efgh.area(),
      "\nПериметр 2-го прямоугольника равна", efgh.perimeter(),
      "\nПлощадь 3-го прямоугольника равна", ijkl.area(),
      "\nПериметр 3-го прямоугольника равна", ijkl.perimeter())
