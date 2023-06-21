# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# Решение:
n = int(input("Введите число N: "))

k = 0
power_of_two = 1

while power_of_two <= n:
    print(power_of_two)
    k += 1
    power_of_two = 2 ** k
