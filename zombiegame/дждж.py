class My_class():
    # свойства_класса
    def __init__(self, a, b):
        self.x = a
        self.y = b

    # методы_класса
    def coordinates(self):
        print('x:', self.x)
        print('y:', self.y)

a = My_class(5,8)
a.coordinates()