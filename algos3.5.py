import random


def partition(array, start, stop):
    b_array, c_start, d_start = array[start], start, start
    for i in range(start + 1, stop):
        if array[i] < b_array:
            c_start += 1
            array[c_start], array[i] = array[i], array[c_start]
            d_start += 1
            if c_start != d_start:
                array[d_start], array[i] = array[i], array[d_start]
        elif array[i] == b_array:
            d_start += 1
            array[d_start], array[i] = array[i], array[d_start]
    array[start], array[c_start] = array[c_start], array[start]
    return c_start, d_start


def randomized_quicksort(array, start, stop):
    if start < stop:
        key = random.randint(start, stop - 1)
        array[start], array[key] = array[key], array[start]
        pivot1, pivot2 = partition(array, start, stop)
        randomized_quicksort(array, start, pivot1)
        randomized_quicksort(array, pivot2 + 1, stop)
        return array

list = []
for i in range(10):
    b = random.randint(1, 10)
    list.append(b)
randomized_quicksort(list, 0, len(list))
index_list = []
for i in range(len(list)):
    key = 0
    if list[i] != 0:
        for c in range(len(list[i:])):
            if list[c] >= list[i] and len(list[i:]) >= list[i]:
                key = 1
            else:
                pass
    if key == 1:
        index_list.append(list[i])
    else:
        pass
index = index_list[len(index_list) - 1]
print('Индекс Хирша =', index)