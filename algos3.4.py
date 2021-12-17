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


with open('input.txt') as f:
    s, p = map(int, f.readline().split())
    a_start, a_end = [], []
    for i in range(s):
        ai, bi = map(int, f.readline().split())
        a_start.append(ai)
        a_end.append(bi)
    points = list(map(int, f.readline().split()))

randomized_quicksort(a_start, 0, len(a_start) - 1)
randomized_quicksort(a_end, 0, len(a_end) - 1)
answer = ''

for point in points:
    count = 0
    for i in range(s):
        if point >= a_start[i]:
            count += 1
        if point > a_end[i]:
            count -= 1
    answer += str(count)
    answer += ' '

with open('output.txt', 'w') as f:
    f.write(answer)

