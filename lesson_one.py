#tps://docs.google.com/presentation/d/123-fQmwW3IQfDVS5F1EPxSl2MgXD8Rpy9bAxOZqHr4o/edit#slide=id.g158afb1c0ed_0_1096
#За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут длиной m километров?
# При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.
#Input:
#n = 700
#m = 750
#Output:
# 2
import math

n = 700
m = 850
#coint_day = m // n
print(m/n)
print(math.ceil(m / n))



#В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для них новыми партами.
# За каждой партой может сидеть два учащихся. Известно количество учащихся в каждом из трех классов.
# Выведите наименьшее число парт, которое нужно приобрести для них.
#Input: 20 21 22(ввод чисел НЕ в одну строку)
#Output: 32

# a = 11
# b = 11
# c = 11
# output = (round(a / 2)) + (round(b / 2)) + (round(c / 2))
# if output % 2 == 0:
#     print(output)
# else:
#     print(output +1)

#Вагоны в электричке пронумерованы натуральными числами, начиная с 1
# (при этом иногда вагоны нумеруются от «головы» поезда, а иногда – с «хвоста»;
# это зависит от того, в какую сторону едет электричка).
# В каждом вагоне написан его номер. Витя сел в i-й вагон от головы поезда и обнаружил,
# что его вагон имеет номер j. Он хочет определить, сколько всего вагонов в электричке.
# Напишите программу, которая будет это делать или сообщать,
# что без дополнительной информации это сделать невозможно.
#Input: 3 4(ввод на разных строках)
#Output: 6

# numberWagon = int(input())
# number_ot_Loko = int(input())
#
# if number_ot_Loko < numberWagon or number_ot_Loko > numberWagon:
#     countWagon = numberWagon + number_ot_Loko
#     print(f'{countWagon} вагонов.')
# else:
#     print(f'Без дополнительной информации это сделать невозможно.')


#Дано натуральное число. Требуется определить, является ли год с данным номером високосным.
# Если год является високосным, то выведите YES, иначе выведите NO.
# Напомним, что в соответствии с григорианским календарем, год является високосным,
# если его номер кратен 4, но не кратен 100, а также если он кратен 400.
#Input: 2016
#Output: YES

# print("Введите год: ")
# a = int(input())
# if a % 4 == 0 and a % 100 != 0 or a % 400 != 0:
#     print("yes")
# else:
#     print('No')

#11.Пользователь вводит целое число. Выведите его строку-описание вида "отрицательное четное число",
# "нулевое число", "положительное нечетное число", например,
# численным описанием числа 190 является строка "положительное четное число".

# print('Введите число: ')
# a = int(input())
# if a < 0:
#     print(f"Число {a} отрицательное.")
# elif a == 0:
#     print(f'Число {a} нулевое.')
# else:
#     print(f'Число  {a} положительное.')





#Шахматный конь ходит буквой "Г" - на две клетки по вертикали в любом направлении
# и на одну клетку по горизонтали, или наоборот. Даны две различные клетки шахматной доски,
# определите, может ли конь попасть с первой клетки на вторую одним ходом.
# В случае, если хотя бы одно из введенных чисел не лежит в диапазоне от 1 до 8, выведите строку "Ошибка!".

# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
# if 1 <= x1 <= 8 and 1 <= x2 <= 8 and 1 <= y1 <= 8 and 1 <= y2 <= 8:
#     if  abs(x2-x1 == 2) and abs(y2-y1 == 1):
#         print('yes')
#     elif abs(x2-x1 == 1) and abs(y2-y1 == 2):
#         print('yes')
#     else:
#         print('no')
# else:
#     print('errer')



#Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника.
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других,
# то треугольника с такими сторонами не существует.

# a = int(input())
# b = int(input())
# c = int(input())
#
# if a + b > c and a + c > b and b + c > a:
#     print('Это треугольник.')
# else:
#     print('Треугольника с такими сторонами не существует.')