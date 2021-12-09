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
    b_array = array[start]
    c_start = start
    for i in range(start + 1, stop + 1):
        if array[i] <= b_array:
            c_start += 1
            array[c_start], array[i] = array[i], array[c_start]
    array[start], array[c_start] = array[c_start], array[start]
    return c_start


with open('input.txt', 'r') as f:
    n, k = map(int, f.readline().split())
    x = [[]] * n
    for i in range(n):
        x[i] = [int(j) for j in f.readline().split()]

a = {}

for i in range(n):
    a[float(((x[i][0] ** 2) + (x[i][1] ** 2)) ** 0.5)] = x[i]

list = [float(key) for key in a]
randomized_quicksort(list, 0, len(list) - 1)

with open('output.txt', 'w') as f:
    for i in range(k-1):
        f.write(str(a[list[i]]))
        f.write(',')
    f.write(str(a[list[k - 1]]))