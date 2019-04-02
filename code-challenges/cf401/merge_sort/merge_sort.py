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
