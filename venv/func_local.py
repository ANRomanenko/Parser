x = 50

r = "romanenko"

def func(x):
    print('x равен', x)
    x = 2
    print('Замена локального х на', x)

func(x)
print('x по прежнему', x)

print(list(r))