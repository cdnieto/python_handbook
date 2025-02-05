# Maximum subarray problem

import numpy as np
import math

data = [-1, 9, 0, 8, -5, 6, -24]


def solucion_1(data):

    suma_max = -np.inf
    i_max = 0
    j_max = 0
    for i in range(len(data)):
        for j in range(i + 1, len(data) + 1):
            suma = np.sum(data[i:j])
            if suma > suma_max:
                suma_max = suma
                i_max = i
                j_max = j - 1

    return [i_max, j_max]


def solucion_2(data):
    start = 0
    end = 0
    global_max = data[0]
    current_max = data[0]

    for i in range(len(data)):

        if current_max + data[i] < data[i]:
            current_max = data[i]
            temp_start = i
        else:
            current_max += data[i]

        if current_max > global_max:
            global_max = current_max
            start = temp_start
            end = i

    return [start, end]


print(solucion_1(data))

print(solucion_2(data))
