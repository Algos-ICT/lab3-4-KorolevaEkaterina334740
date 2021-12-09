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

if __name__ == "__main__":
    list = []
    for i in range(10):
        array = random.randint(1, 100)
        list.append(array)
    print('Неотсортированный массив:', *list)
    randomized_quicksort(list, 0, len(list))
    print('  Отсортированный массив:', *list)

'''with open('input.txt', 'w') as f:
    f.write(str(5))
    for i in range(10):
        f.write(str(random.randint(1, 100)))
with open('input.txt') as f:
    n = int(f.readline())
    list = f.readline()
list = list.split()
for i in range(n):
    list[i] = int(list[i])
print('Неотсортированный массив:', *list)
randomized_quicksort(list, 0, len(list))
with open('output.txt', 'w') as f:
    f.write(list)
print('  Отсортированный массив:', *list)'''
