shop = ['Mercedes', 'Volkswagen', 'Audi']

print('Я должен сделать', len(shop), 'покупки')

print('Покупки:', end=' ')
for item in shop:
    print(item, end=' ')

print('\nТакже нужно купить BMW')
shop.append('BMW')
print('Теперь мой список покупок таков', shop)
print('Отсортирую-ка я свой список')
shop.sort()
print('Отсортированный список покупок выглядит так', shop)

print('Первое что мне нужнок упить это', shop[0])
olditem = shop[0]
del shop[0]
print('Я купил', olditem)
print('Теперь мой список покупок:', shop)

zoo = ('Слон', 'Жираф')

print('В зоопарке', len(zoo), 'зверей')

new_zoo = 'Кабан', 'Черепаха', zoo

print('В новом зоопарке', len(new_zoo), 'клетки')