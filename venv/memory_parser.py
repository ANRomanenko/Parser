shop = ['Mercedes', 'Volkswagen', 'Audi']

print('Я должен сделать', len(shop), 'покупки')

print('Покупки:', end='')
for item in shop:
    print(item, end='')

print('\nТакже нужно купить BMW')
shop.append('BMW')
print('Теперь мой список покупок таков', shop)
print('Отсортирую-ка я свой список')
shop.sort()
print('Отсортированный список покупок выглядит так', shop)

print('Первое ')