"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""


def string_comparison(first_string: str, second_string: str):
    if isinstance(first_string, str) and isinstance(second_string, str):
        if first_string == second_string:
            return 1
        else:
            if 'learn' in second_string:
                return 3
            elif len(first_string) > len(second_string):
                return 2
            else:
                return 'Не выполнено ни одно из условий'
    else:
        return 'На вход поданы неверные данные'


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    """
    print(string_comparison('python', 'python'))
    print(string_comparison('string', 'kek'))
    print(string_comparison('learn', 'python'))
    print(string_comparison('python', 'learn'))
    print(string_comparison('string', 5 ))


if __name__ == "__main__":
    main()
