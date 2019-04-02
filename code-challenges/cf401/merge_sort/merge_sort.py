def merge_sort(list):
    """

    """
    f1 = 0
    e1 = ((len(list) - f1) // 2) + f1
    f2 = e1 + 1 if e1 != len(list) - 1 else None
    e2 = len(list) - 1 if f2 is not None else None

    def _divide(front, end, list):
        if end - front > 1:
            end = (end - front) // 2
            _divide(front, end)
        if list[end] > list[front]:
            curr_end = end
            list[end], list[front] = list[front], list[end]


# 1. length = 3 | list[3] - list[] | list[] - list[]