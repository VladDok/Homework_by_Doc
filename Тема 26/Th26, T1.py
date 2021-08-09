import random

list_of_items = [random.choice(range(100)) for _ in range(100)]
list_of_items.sort()

def binary_search(items, item):
    mid = len(items) // 2
    start = 0
    finish = len(items) - 1

    if item == items[mid]:
        return True

    elif start == finish:
        return False

    elif item < items[mid]:
        items = items[:mid]
        return binary_search(items, item)

    elif item >= items[mid]:
        items = items[mid:]
        return binary_search(items, item)


print(binary_search(list_of_items, 29))
