what = input('Что делать? (+, -, *,  /): ')

a = float(input('Ввведите первое значение: '))
b = float(input('Введите второе значение: '))

if what == '+':
    print('Ответ:', a + b)
elif what == '-':
    print('Ответ:', a - b)
elif what == '*':
    print('Ответ:', a * b)
elif what == '/':
    print('Ответ:', a / b)
else:
    print('Внесено не правильное значение!')