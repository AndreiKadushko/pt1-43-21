"""
Определите, является ли число палиндромом (читается слева направо и справа
налево одинаково). Число положительное целое, произвольной длины. Задача
требует работать только с числами (без конвертации числа в строку или что-нибудь
еще)
"""
A = int(input('Введите число: '))
Inv_A = 0
Ost = A
while Ost > 0:
    Inv_A = Inv_A * 10 + Ost % 10
    Ost = Ost // 10
if A == Inv_A:
    print('Число', A, 'палиндром')
else:
    print('Число', A, 'не палиндром')