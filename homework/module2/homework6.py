# Дополнительное практическое задание по модулю: "Базовые структуры данных."
"""
Задание "Слишком древний шифр":
Вы отправились в путешествие на необитаемый остров и конечно же в очередной вылазке в джунгли вы попали в ловушку
местному племени (да-да, классика "Индиана Джонса").
К вашему удивлению, в племени были неплохие математики и по совместительству фантазёры.
Вы поняли это, когда после долгих блужданий перед вами появились ворота (выход из ловушки) с двумя каменными
вставками для чисел.
В первом поле камни с числом менялись постоянно (от 3 до 20) случайным образом, а второе было всегда пустым.

К вашему счастью рядом с менее успешными и уже неговорящими путешествинниками находился попирус, где были написаны
правила для решения этого "ребуса". (Как жаль, что они поняли это так поздно :( ).

Во вторую вставку нужно было написать те пары чисел друг за другом, чтобы число из первой вставки было кратно
сумме их значений.

Пример 1:
9 - число из первой вставки
18273645 - нужный пароль (1 и 8, 2 и 7, 3 и 6, 4 и 5 - пары; число 9 кратно сумме каждой пары)

Пример 2:
11 - число из первой вставки
11029384756 - нужный пароль (1 и 10, 2 и 9, 3 и 8, 4 и 7, 5 и 6 - пары; число 11 кратно сумме каждой пары)


К сожалению, у вас не так много времени, чтобы подбирать пароль вручную, шипы сверху уже движуться на вас
(обожаю клише), тем более числа в первой вставке будут попадаться случайно.

Составьте алгоритм, используя циклы, чтобы в независимости от введённого числа n (от 3 до 20) программа выдавала
нужный пароль result, для одного введённого числа.

Что является парой?:
Пары являются уникальными на примере следущего:
7 3 3 5 8
В этой последовательности уникальными парами являются:
Для первой 7: 73 73 75 78
Для второй 3: 33 35 38 (с пеервой 7 у этой 3 уже есть пара, поэтому её не берём).

Все пароли для чисел от 3 до 20 (для сверки):
3 - 12
4 - 13
5 - 14 23
6 - 12? 15 24
7 - 16 25 34
8 - 13? 17 26 35
9 - 12? 18 27 36 45
10 - 141923 28 37 46
11 - 110 29 38 47 56
12 - 12131511124 210 39 48 57
13 - 112211310495867
14 - 1611325212343114105968
15 - 1214114232133124115106978
16 - 1317115262143531341251161079
17 - 11621531441351261171089
18 - 12151811724272163631545 4+14+5+13 6+12 7+11 8+10
19 - 1+18 2+17 3+16 4+15 5+14 6+13 7+12 8+11 9+10
20 - 13141911923282183731746 4+16 5+15 6+14 7+13 8+12 9+11


Примечания:
Можно использовать как цикл for, так и цикл while
Первое число не входит в одно из чисел пары
Пары чисел подбираются от 1 до 20 для текущего числа.
"""


random_number = list(range(3, 21))  # создаст последовательность чисел от 3 до 20

# # Решение через for
# for i in random_number:
#     pairs = []
#     for j in range(1, 21):
#         for k in range(1, 21):
#             if i == j + k:
#                 pairs += [[j, k]]
#         if len(pairs) > 1 and pairs[-1][0] == pairs[-2][-1]:  # проверка для нечётных [x, y][y, x]
#             pairs.remove(pairs[-1])  # удалит последнюю записанную пару
#             break
#         if len(pairs) > 1 and pairs[-1][-1] == pairs[-1][-2]:  # проверка для чётных. [x, x]
#             pairs.remove(pairs[-1])
#             break
#     print(f'{i} - {pairs}')
#
#
#
#
#
# lisy_ = [[60, 77], [1, 2, 3], [4, 5], [5, 4]]
# if sum(lisy_[-1]) == sum(lisy_[-2]):
#     print('true')
# if len(lisy_) > 2:
#     print('yes')
# if lisy_[-2][-1] == lisy_[-1][0]:
#     print('pip')

# for num in random_number:
#     print(f'число в первом поле {num}')
#     for i in range(1, num // 2 + 1):  # 1,  4 // 2 == 3
#         if (num - i) % num == 2 or 3:  # 4 - 2 % 4 == 2
#             print(f'{i}, {num - i}')  # 1, 8

num = int(input("Введите число от 3 до 20: "))

for i in range(1, num):
    for j in range(i + 1, num):
        if (i + j) % num == 0:
            print(f"{i} и {j}")

while num < 21:
