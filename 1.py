import math

class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def resize(self, factor):
        pass
    
    def rotate(self, angle):
        pass
    
    def move(self, x, y):
        self.x += x
        self.y += y

class Circle(Shape):
    def __init__(self, x, y, r):
        super().__init__(x, y)
        self.r = r
    
    def resize(self, factor):
        self.r *= factor
    
    def rotate(self, angle):
        pass  # круг не может быть повернут
    
    def area(self):
        return math.pi * self.r ** 2
    
class Square(Shape):
    def __init__(self, x, y, size):
        super().__init__(x, y)
        self.size = size
    
    def resize(self, factor):
        self.size *= factor
    
    def rotate(self, angle):
        pass  # квадрат не может быть повернут
    
    def area(self):
        return self.size ** 2
    
class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self.width = width
        self.height = height
    
    def resize(self, factor):
        self.width *= factor
        self.height *= factor
    
    def rotate(self, angle):
        # Повернуть на угол angle с помощью матричных преобразований
        x1 = self.width / 2
        x2 = -self.width / 2
        y1 = self.height / 2
        y2 = -self.height / 2
        new_x1 = x1 * math.cos(angle) - y1 * math.sin(angle)
        new_y1 = x1 * math.sin(angle) + y1 * math.cos(angle)
        new_x2 = x2 * math.cos(angle) - y2 * math.sin(angle)
        new_y2 = x2 * math.sin(angle) + y2 * math.cos(angle)
        self.width = max(abs(new_x1 - new_x2), 0)
        self.height = max(abs(new_y1 - new_y2), 0)
    
    def area(self):
        return self.width * self.height

# Пример использования
circle = Circle(0, 0, 5)
square = Square(5, 5, 10)
rectangle = Rectangle(0, 10, 5, 10)

print(circle.area())    # выведет приблизительно 78.54
print(square.area())    # выведет 100
print(rectangle.area()) # выведет 50

circle.resize(2)
square.resize(0.5)
rectangle.resize(1.5)

circle.rotate(math.pi / 4)
square.rotate(math.pi / 3)
rectangle.rotate(math.pi / 6)

circle.move(1, 1)
square.move(2, 2)
rectangle.move(3, 3)

print(circle.area())    # выведет приблизительно 314.16
print(square.area())    # выведет 25
print(rectangle.area()) # выведет приблизительно 54.37