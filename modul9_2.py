def create_operation(operation):
    if operation == "multiply":
        def multiply(x, y):
            return x * y
        return multiply
    elif operation == "share":
        def share(x, y):
            return x / y
        return share
my_func_multiply = create_operation("multiply")
my_func_share = create_operation('share')
print('Фабрика функций')
print(my_func_multiply(2,3))
print(my_func_share(6,3))


multiply = lambda x: x ** 2
print('лямбда')
print(multiply(5))

def multiply_def(x):
   return x ** 2
print(multiply_def(7))

class Rect:
   def __init__(self, a, b):
       self.a = a
       self.b = b
   def __call__(self, a, b):
       return a * b

square = Rect(2, 3)


print('Вызываемые объекты')
print("Стороны:")# не знаю как записать стороны
print('Площадь:', square(2, 3))