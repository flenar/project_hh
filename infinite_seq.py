# -*- coding: utf-8 -*-
"""
Created on Sat Sep 13 20:25:16 2014

@author: Lenar
Бесконечная последовательность
Возьмём бесконечную цифровую последовательность, образованную склеиванием последовательных положительных чисел: S = 123456789101112131415...
Определите первое вхождение заданной последовательности A в бесконечной последовательности S (нумерация начинается с 1).

Пример входных данных:
6789
101

Пример выходных данных:
6
10
"""

def first_in_infinite():
    """
    Функция запускает бесконечный цикл, в каждой итерации которого к последовательности
    добавляется одна цифра и происходит проверка на факт наличия искомой последовательности в бесконечной последовательности.
    Ищем каждый раз не во всей строке, а только в той её части, где были добавлены новые данные.
    Когда подстрока находится цикл бесконечной последовательности останавливается.
    """
    given_sequence = input()
    infinite_sequence = ""
    next_int = 0
    while 1:
        next_int += 1
        next_int_str = str(next_int)
        infinite_sequence += next_int_str
        start_pos = len(infinite_sequence) - len(next_int_str) - len(given_sequence) + 1 #немного оптимизируем поиск, т.к. нам не нужно каждый раз искать во всей строке
        if start_pos < 0:
            start_pos = 0
        position = infinite_sequence.find(given_sequence, start_pos) # ищем только там, где были добавлены данные и может появиться наше число
        if position <> -1: # когда наконец нашли - заканчиваем цикл и выдаем позицию
            print position + 1
            return 0


def input():
    while 1:
        go_on = True
        seq = raw_input("Input your int sequence (press Enter to exit):")
        if seq == "":
            return 0
        for ch in range(0,len(seq)):
            try:
                int(seq[ch])
            except:
                print "Wrong sequence, please enter positive integers..."
                go_on = False
                break
        if go_on:
            return seq

first_in_infinite()