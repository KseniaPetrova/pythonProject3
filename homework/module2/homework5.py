# функции можно разделить на несколько видов: обычные, принимающие, возвращающие и анонимные.
# Принимающая – это та функция, в момент создания которой мы определяем какое-то значение, которые она будут принимать,
# а значит в момент вызова функции мы также должны будем его передать.
# возвращающая – это та функция, которая нам что-то возвращает. А возвращать что-то она будет с помощью команды return.

"""
Создайте функцию def print_params, которая в своем теле будет распечатывать переданное значение из параметра 2 раза!
Вызовите данную функцию несколько раз в том же файле
Запустите поэтапное выполнение программы, нажмите на иконку дебага справа от запуска проекта "жучок"
В консоли посмотрите на результат программы
Используйте Step Over (см. скриншот) для перехода к следующему шагу выполнения программы
Посмотрите на консоль и на ход выполнения программы
"""

def print_params(enter):
    print(enter, enter)

print_params('hello')
print_params('Its me')
print_params(666)