# Калькулятор V1

what = input( "Что делать? (+, -, *, /): " )

a = float(input("Введи первое число: "))
b = float(input("Введи второе число: "))

if what == "+":
    print("Ответ", a + b)
elif what == "-":
    print("Ответ", a - b)
elif what == "*":
    print("Ответ", a * b)
elif what == "/":
    print("Ответ", a / b)
else:
    print("Выбрана неверная операция!")
