def binary_search(arr, val):
    count = len(arr)
    midpoint = count // 2
    start_index = 0
    end_index = count - 1

    while val != arr[midpoint] and count > 1:
        if val > arr[midpoint]:
            start_index = midpoint
            count = count - midpoint
            midpoint = count // 2 + start_index
        else:
            end_index = midpoint
            count = count - midpoint
            midpoint = count // 2 + start_index

    if val == arr[midpoint]:
        return midpoint
    else:
        return -1

# [1, 2, 4, 7], 7
