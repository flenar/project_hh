# -*- coding: utf-8 -*-

"""

@author: Lenar

Выпуклая оболочка
Дан набор точек на плоскости. Постройте минимальную выпуклую оболочку для данного набора.
Каждая точка имеет номер, равный порядковому номеру точки во входных данных (начиная с 1). 
Минимальную выпуклую оболочку можно описать как последовательность точек на пересечении её границ (начальная точка может быть выбрана произвольно).

Пример входных данных:
2 3
4 4
3 7
6 5
7 2

Пример выходных данных:
1 3 4 5
"""

def points_input():
    """
    Функция ввода исходных точек. Входящих значений нет, возвращает - лист кортежей точек.
    """
    points_list = []
    while 1:
        new_point = raw_input("Enter new coordinates through space (Empty line to exit):")
        if new_point == "":
            break
        try:
            point_pair_tuple = tuple()
            point_pair_list = new_point.split()
            point_pair_tuple = (int(point_pair_list[0]), int(point_pair_list[1]))
        except:
            print("Wrong coordinates, please try again...")
            continue
        points_list.append(point_pair_tuple)
    return points_list


def convex_hull():
    """
    Алгоритм основан на следующем:
    1. Берем самую нижнюю точку, выбрав её первой в выпуклой оболочке. (58-64)
    2. Далее по часовой стрелке измеряем полярный угол против часовой стрелки каждой из точек, взяв за центр текущую точку. 
    Точку с максимальным полярным углом добавляем в нашу последовательность точек и делаем её 
    текущей для следующей итерации. Таким образом находим все точки из левой половины оболочки вплоть до самой верхней.
    Начиная с самой верхней точки (max Y) начинаем измерять обратные полярные углы, по часовой стрелке. 
    Углы получаются минусовые, поэтому по тому же условию максимального угла добавляем точки из второй половины.
    Функция печатает последовательность точек минимальной выпуклой оболочки.
    """
    points_list = points_input()
    if len(points_list) == 0:
        return 0
    # ищем отправную точку, выбрав точку с минимальным Y (minimum_y) во введенном наборе. Если их больше одной - берется первая.
    # ищем отправную точку для второй половины поиска (maximum_y), т.к. снизу справа вверх углы идут плюсовые, а сверху слева вниз - негативные.
    minimum_y = points_list[0]
    maximum_y = points_list[0]
    for indx in range(0, len(points_list)):
        if minimum_y[1] > points_list[indx][1]:
            minimum_y = points_list[indx]
        if maximum_y[1] < points_list[indx][1]:
            maximum_y = points_list[indx]

    # результирующий лист
    result_list = [minimum_y]

    import math
    next_point = points_list[0]
    negative_degrees = False #флаг начала второй половины поиска, с негативными углами
    while 1:
        max_angle = math.pi * -2 #-360 градусов, минимум
        for indx in range(0, len(points_list)):
            if result_list[-1] == points_list[indx]: #не сравниваем точку саму с собой
                continue
            next_atan2 = math.atan2(points_list[indx][1] - result_list[-1][1], points_list[indx][0] - result_list[-1][0]) # вычисляется угол, поставив на центр координат последнюю текущую точку в выпуклой оболочке

            #Корректировка показателей углов, приведение к общему направлению
            if not negative_degrees:  # во время подъема наверх
                if next_atan2 < 0:    # если встречаются минусовые углы (точки ниже текущей)
                    next_atan2 = 2 * math.pi + next_atan2  # переворачиваем такой угол в плюсовой
            elif next_atan2 > 0:      # во время спуска
                next_atan2 = next_atan2 - 2 * math.pi  # переворачиваем все плюсовые углы в минусовые

            if next_atan2 > max_angle:
                if (not negative_degrees and next_atan2 <= math.pi) or (negative_degrees and next_atan2 >= -1 * math.pi): # во время подъёма не учитываем точки ниже текущей, во время спуска - точки выше текущей
                    max_angle = next_atan2
                    next_point = points_list[indx]

        if next_point == minimum_y:  # доходим до стартовой точки - цикл завершен
            break
        if next_point == maximum_y:  # доходим до самой верхней точки - начинаем набирать левую половину
            negative_degrees = True
        result_list.append(next_point)
    # Вывод результата в необходимом виде:
    for point in range(0, len(result_list)):
        print points_list.index(result_list[point]) + 1,
    return 0
    

convex_hull()

