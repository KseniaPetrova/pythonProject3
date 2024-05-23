'''
"Строки и индексация строк"

Используя индексацию строк, выполните следующие действия со строкой - 'это моя строка'
(должно быть 6 вызовов print в коде):
1. Выведите первый символ.
2. Выведите последний символ (используя отрицательный индекс).
3. Выведите подстроку с третьего по пятый символы (то есть со второго по четвёртый индекс.
Важно помнить что в записи [4:8] выведется с 4 по 7 индекс).
4. Выведите строку наоборот
5. Выведите длину строки (функция len).
6. Соедините строки 'это новая строка' и 'это моя строка' (в той же последовательности)
и выведите результат на экран.
'''

string = 'это моя строка'
stringNew = 'это новая строка'
print('1. ' + string[0])  # э
print('2. ' + string[-1])  # а
print('3. ' + string[2:5])  # о м
print('4. ' + string[::-1])  # акортс яом отэ
print('5. ' + str(len(string)))  # 14
print('6. ' + stringNew + ' ' + string)  # это новая строка это моя строка

# test
print(string[:-1])  # это моя строк

