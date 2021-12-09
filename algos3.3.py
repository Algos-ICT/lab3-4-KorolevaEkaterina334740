import random


def randomized_quicksort(array, start, stop):
    if start < stop:
        key = random.randint(start, stop)
        array[start], array[key] = array[key], array[start]
        pivot = partition(array, start, stop)
        randomized_quicksort(array, start, pivot - 1)
        randomized_quicksort(array, pivot + 1, stop)
    return array


def partition(array, start, stop):
    b_array, c_start = array[start][0], start
    for i in range(start + 1, stop + 1):
        if array[i][0] <= b_array:
            c_start += 1
            array[c_start], array[i] = array[i], array[c_start]
    array[start], array[c_start] = array[c_start], array[start]
    return c_start


def game(array):
    if array == 1:
        return 'YES'
    for i in range(n):
        b = 0
        c = 0
        while c < len(a[list[i][0]]):
            if abs(i - a[list[i][0]][c]) % array == 0:
                b += 1
                a[list[i][0]].pop(c)
            c += 1
        if (b == 0):
            return 'NO'
    return 'YES'


with open('input.txt') as f:
    n, k = map(int, f.readline().split())
    list = [int(x) for x in f.readline().split()]

a = {}
for i in range(n):
    list[i] = [int(list[i]), i]
    a[list[i][0]] = a.get(list[i][0], [])
    a[list[i][0]].append(list[i][1])

randomized_quicksort(list, 0, len(list) - 1)

with open('output.txt', 'w') as f:
    f.write(game(k))