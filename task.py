import random

# # Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

number = input('введите число: ')
sum = 0
for i in number:
    if i != '.':
        sum += int(i)
print(sum)


# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

N = int(input('введите число: '))
first = 1
numbers = range(1, N)
for i in numbers:
    first *= i
    print(first, end=', ')
print(first*N)

# Задайте список из n чисел последовательности (1 + 1/n) ** n и выведите на экран их сумму.

n = int(input('введите число: '))
someList = []
i = 1
while i <= n:
    someList.append(round(((1+1/i)**i), 2))
    i += 1
print(someList)
summa = sum(someList)
print(f'Сумма элементов списка: {round(summa,2)}')

# Реализуйте алгоритм перемешивания списка.
listt = [1, 41, 'gg', -1, 0, '*']
print(f'изначальный список: {listt}')
random.shuffle(listt)
print(f'перемешанный список: {listt}')
