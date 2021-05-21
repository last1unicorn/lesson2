"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

lod_students_marks = [
    {'school_class': '4a', 'scores': [3, 4, 5, 3, 2]},
    {'school_class': '5b', 'scores': [3, 5, 4, 5, 2]},
    {'school_class': '6c', 'scores': [3, 2, 3, 5, 1]},
    {'school_class': '7d', 'scores': [3, 4, 2, 5, 2]},
]


def each_class_marks(lod_students_marks: list):
    for dictionary in lod_students_marks:
        school_class = dictionary['school_class']
        print(f'Средний балл по классу {school_class} :'+str(sum(dictionary['scores'])/len(dictionary['scores'])))


def medium_school_scores(lod_students_marks: list, total=0):
    for dictionary in lod_students_marks:
        total += sum(dictionary['scores'])/len(dictionary['scores'])
    print('Средний балл по всей школе:   '+str(total / len(lod_students_marks)))


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    """
    each_class_marks(lod_students_marks)
    medium_school_scores(lod_students_marks)


if __name__ == "__main__":
    main()
