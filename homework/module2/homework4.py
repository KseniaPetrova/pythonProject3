"""
Создайте список из 5 машин - ["BMW", "MB", "LADA", "KIA", "HONDA"]
Создайте цикл for и в цикле распечатайте каждый из автомобилей в строке 'Я езжу на автомабиле марки'
Создайте целочисленную переменную cars_count = 0
Напишите в цикле из шага номер 2 увеличение переменной на 10 в каждом шаге цикла (cars_count += 10)
Посмотрите на консоль и на ход выполнения программы
"""

# cars = list(["BMW", "MB", "LADA", "KIA", "HONDA"])
# cars_count = 0
# for i in cars:
#     print('Я езжу на автомабиле марки', i )
#     cars_count += 10
#     print(cars_count)

"""
Задача "Всё не так уж просто":
Дан список чисел  numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
Используя этот список составьте второй список primes содержащий только простые числа.
А так же третий список not_primes, содержащий все не простые числа.
Выведите списки primes и not_primes на экран(в консоль).
Пункты задачи:
Создайте пустые списки primes и not_primes.
При помощи цикла for переберите список numbers.
Напишите ещё один цикл for (вложенный), где будут подбираться делители для числа из 1ого цикла.
Отметить простоту числа можно переменной is_prime, записав в неё занчение True перед проверкой.
В процессе проверки на простоту записывайте числа из списка numbers в списки primes и not_primes в зависимости 
от значения перменной is_prime после проверки (True - в prime, False - в not_prime).
Выведите списки primes и not_primes на экран(в консоль).

Пример результата выполнения программы:
Исходный код:
 numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
Вывод на консоль:
Primes: [2, 3, 5, 7, 11, 13]
Not Primes: [4, 6, 8, 9, 10, 12, 14, 15]
Примечания:
Учтите, что число 1 не является ни простым, ни составным числом, поэтому оно отсутствует в конечных списках.
Для проверки на простоту числа вам нужно убедиться, что выбранное число не делиться ни на что в диапазоне 
от 2 до этого числа(не включительно).
Попробуйте оптимизировать(ускорить) процесс выяснения простоты числа при помощи оператора break, 
когда найдёте делитель. (Не обязательно)
Переменные меняющее своё булевое состояние на противоположное в процессе проверки, как is_prime, 
в кругах разработчиков называются перменными-флагами(flag).

"""
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# primes = []  # [2, 3, 5, 7, 11, 13]
# not_primes = []  # [4, 6, 8, 9, 10, 12, 14, 15]
# is_prime = True  # после проверки (True - в prime, False - в not_prime).
# for i in numbers:
#     test = []
#     if i == 1:
#         continue
#     for j in numbers:
#         if i % j == 0:
#             test += [j]
#     if len(test) < 3:
#         primes += [i]
#     else:
#         not_primes += [i]
# print(primes)
# print(not_primes)

#решение с флагом is_prime

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []  # [2, 3, 5, 7, 11, 13]
not_primes = []  # [4, 6, 8, 9, 10, 12, 14, 15]

for i in numbers:
    is_prime = True  # после проверки (True - в prime, False - в not_prime).
    test = []
    if i == 1:
        continue
    for j in numbers:
        if i % j == 0:
            test += [j]
        if len(test) < 3:
            is_prime = True
            break
    else:
        is_prime = False
    if is_prime:
        primes += [i]
    else:
        not_primes += [i]
print(primes)
print(not_primes)





# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
#
# primes = []
# not_primes = []
#
# for num in numbers:
#     is_prime = True
#
#     if num <= 1:
#         is_prime = False
#     else:
#         for i in range(2, int(num ** 0.5) + 1):
#             if num % i == 0:
#                 is_prime = False
#                 break
#
#     if is_prime:
#         primes.append(num)
#     else:
#         if num != 1:
#             not_primes.append(num)
#
# print("Простые числа:", primes)
# print("Не простые числа:", not_primes)
