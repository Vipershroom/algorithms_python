import random

def bubble_sort(arr):
    for i in range(len(arr) -1):
        for k in range(i +1, len(arr)):
            if arr[i] > arr[k]:
                arr[i], arr[k] = arr[k], arr[i]

    return arr

test_case = [i for i in range(99999)]

random.shuffle(test_case)

print(bubble_sort(test_case))
