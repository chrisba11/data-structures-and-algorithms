from ..stacks_and_queues.stacks_and_queues import Queue, Node


def radix_sort(list):
    """
    Takes in a list and returns a new sorted version of the same list using a radix sort method.
    """
    queues = [Queue() for i in range(10)]
    max_val = max(list) if len(list) > 0 else 0
    iterations = len(str(max_val))
    loop_num = 0

    def _radix_sort(list):
        """
        This function is what is called recursively to sort the list by ones, tens, hundreds, etc. each time it is called.
        """
        nonlocal iterations
        nonlocal loop_num

        while loop_num < iterations:
            output = []
            for num in list:
                q = num // (10 ** loop_num) % 10
                queues[q].nq(num)

            for queue in queues:
                while queue.front:
                    output.append(queue.dq())

            loop_num += 1

            return _radix_sort(output)

        return list

    return _radix_sort(list)
