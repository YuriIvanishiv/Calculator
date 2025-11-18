class Calculator:
    def add (self, a, b):
        return a + b
    def subtract (self, a, b):
        return a - b
    def multiply (self, a, b):
        return a * b
    def divide (self, a, b):
        if b == 0:
            return "Ошибка: Деление на 0"
        return a / b
Calculator = Calculator()
print(Calculator.add(7, 10))
print(Calculator.subtract(99, 31))
print(Calculator.multiply( 13, 2))
print(Calculator.divide(1, 0))