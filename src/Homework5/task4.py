"""
Даны два списка чисел. Посчитайте, сколько различных
чисел входит только в один из этих списков
"""

set_number_1 = (set(int(x) for x in
                    input('Введите первый список чисел через пробел: ').
                    split()))
set_number_2 = (set(int(x) for x in
                    input('Введите второй список чисел через пробел: ').
                    split()))
print('Количество различных чисел в первом списке: ',
      len(set_number_1 - set_number_2))
