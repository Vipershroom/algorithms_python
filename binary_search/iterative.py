def binary_search(num_list, target):
    first = -1
    last = len(num_list)
    iterCheck = 0

    while first + 1 != last:
        half = (first + last) // 2

        if num_list[half] == target:
            return half
        elif num_list[half] > target:
            last = half
        else:
            first = half 
    return -1


test_case = [1,2,4,8,25, 27, 29, 30]
print(binary_search(test_case, 1))