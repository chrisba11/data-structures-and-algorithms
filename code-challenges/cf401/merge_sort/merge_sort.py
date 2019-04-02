def merge_sort(list):
    """
    Takes in a list and sorts it using merge sort logic. Returns the list.
    """
    def _divide(list, front=0):
        """
        Adjusts the starting and ending point of the array to narrow down the number of elements to sort.
        """
        f1 = front
        e1 = ((len(list) - f1) // 2) + f1
        f2 = e1 + 1 if e1 != len(list) - 1 else None
        e2 = len(list) - 1 if f2 is not None else None

        if end - front > 1:
            end = (end - front) // 2
            _divide(front, end)
        if list[end] > list[front]:
            curr_end = end
            list[end], list[front] = list[front], list[end]





# def merge(left, right):
#     """Merge sort merging function."""

#     left_index, right_index = 0, 0
#     result = []
#     while left_index < len(left) and right_index < len(right):
#         if left[left_index] < right[right_index]:
#             result.append(left[left_index])
#             left_index += 1
#         else:
#             result.append(right[right_index])
#             right_index += 1

#     result += left[left_index:]
#     result += right[right_index:]
#     return result


# def merge_sort(array):
#     """Merge sort algorithm implementation."""

#     if len(array) <= 1:  # base case
#         return array

#     # divide array in half and merge sort recursively
#     half = len(array) // 2
#     left = merge_sort(array[:half])
#     right = merge_sort(array[half:])

#     return merge(left, right)