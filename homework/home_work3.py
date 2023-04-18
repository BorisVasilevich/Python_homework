# Урок 3. Списки и словари
# Задача 16:
# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
#
# 5
#     1 2 3 4 5
#     3
#     -> 1
import random
a = int(input('Введите число от 0 до 5: '))
mas = [random.randint(0, 5) for i in range(10)]
print(mas)
count = 0
for i in mas:
    if i == a:
        count +=1
print(count)

# Задача 18: Требуется найти в массиве A[1..N] самый близкий
# по величине элемент к заданному числу X. Пользователь в первой
# строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

import random
a = int(input('Введите число от 0 до 50: '))
mas = [random.randint(0, 50) for i in range(10)]
print(mas)
x = 0
y = 50
w = -1
for i in range(len(mas)):
    if mas[i] == a:
        w = mas[i]
        print(f'самый близкий по величине элемент к заданному числу {a}.')
        break
    if mas[i] < a and x < mas[i]:
        x = mas[i]
    if mas[i] > a and y > mas[i]:
        y = mas[i]

if w == a:
    print("The End")
else:
    if (a - x) > (y - a):
        print(f'самый близкий по величине элемент к заданному числу {y}.')
    if (a - x) < (y - a):
        print(f'самый близкий по величине элемент к заданному числу {x}.')
    if (a - x) == (y - a):
        print(f'самый близкий по величине элемент к заданному числу {x} and {y}.')



# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая
# буква имеет определенную ценность. В случае с английским
# алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка; B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо
# только английские, либо только русские буквы.
#
# *Пример:*
# ноутбук
#     12


lis = {'А': 1, 'В': 1, 'Е': 1, 'И': 1, 'Н': 1, 'О': 1, 'Р': 1, 'С': 1, 'Т': 1, 'Д': 2, 'К': 2, 'Л': 2, 'М': 2,
       'П': 2, 'У': 2, 'Б': 3, 'Г': 3, 'Ё': 3, 'Ь': 3, 'Я':3, 'Й': 4, 'Ы': 4, 'Ж': 5, 'З': 5, 'Х': 5, 'Ц': 5,
       'Ч': 5, 'Ш': 8, 'Э': 8, 'Ю': 8, 'Ф': 10, 'Щ': 10, 'Ъ': 10
       }

list1 = str(input('Введите слово.'))
point = 0
for i in list1:
    for key, value in lis.items():
        if i == key:
            point = point + value
print(point)