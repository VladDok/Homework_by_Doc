from timeit import timeit

def fibonacci_search(list, item):
    fibM_minus_2 = 0
    fibM_minus_1 = 1
    fibM = fibM_minus_1 + fibM_minus_2
    while (fibM < len(list)):
        fibM_minus_1, fibM_minus_2 = fibM, fibM_minus_1
        fibM = fibM_minus_1 + fibM_minus_2
    index = -1
    while (fibM > 1):
        i = min(index + fibM_minus_2, (len(list)-1))
        if (list[i] < item):
            fibM, fibM_minus_1 = fibM_minus_1, fibM_minus_2
            fibM_minus_2 = fibM - fibM_minus_1
            index = i
        elif (list[i] > item):
            fibM = fibM_minus_2
            fibM_minus_1 = fibM_minus_1 - fibM_minus_2
            fibM_minus_2 = fibM - fibM_minus_1
        else :
            return i
    return False

def binary_search(array, item):
    first = 0
    last = len(array) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if array[midpoint] == item:
            found = True
        else:
            if item < array[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    return found


def sequential_search(array, item):
    pos = 0
    found = False
    while pos < len(array) and not found:
        if array[pos] == item:
            found = True
        else:
            pos = pos + 1
    return found

def search_min_value(time1, time2, time3):
    min_value = min(time1, time2, time3)
    if time1 == min_value:
        return 'Fibonacci'
    elif time2 == min_value:
        return 'binary'
    else:
        return 'sequential'


fib_time = timeit(
    stmt= "fibonacci_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 6)",
    number = 1000,
    setup= "from __main__ import fibonacci_search"
)

bin_time = timeit(
    stmt= "binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 6)",
    number= 1000,
    setup= "from __main__ import binary_search"
)

seq_time = timeit(
    stmt= "sequential_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 6)",
    number = 1000,
    setup= "from __main__ import sequential_search"
)

print(f'Time for Fibonacci search: {fib_time}.\nTime for binary search: {bin_time}.\nTime for sequential search: {seq_time}.\n')

print(f'Result: the fastest algorithm is {search_min_value(fib_time, bin_time, seq_time)}.')



