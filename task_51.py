"""
Напишите функцию same_by(characteristic, objects), которая
проверяет, все ли объекты имеют одинаковое значение
некоторой характеристики, и возвращают True, если это так.
Если значение характеристики для разных объектов
отличается - то False. Для пустого набора объектов, функция
должна возвращать True. Аргумент characteristic - это
функция, которая принимает объект и вычисляет его
характеристику.
Ввод: 
values = [0, 2, 10, 6] 
if same_by(lambda x: x % 2, values):
print(‘same’)
else:
print(‘different’)

Вывод:
same
"""
values = [1, 21, 11, 63]
def same_by(deff, values):
    defValues = []
    for i in values:
        defValues.append(deff(i))
    count = 0
    for i in defValues:
        if i != defValues[1]:
            count+=1
    if count == 0: return True
    else: return False 
    


if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')

