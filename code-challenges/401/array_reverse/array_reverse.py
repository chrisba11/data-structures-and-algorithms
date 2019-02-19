array_before = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def reverse_array(arr):
    arr2 = []
    for i in range(len(arr), 0, -1):
        arr2.append(arr[i-1])
    return arr2


array_after = reverse_array(array_before)

print(array_after)
