from ..stacks_and_queues.stacks_and_queues import Queue


def radix_sort(list):
    queues = [Queue() for i in range(10)]
    max_val = max(list)
    iterations = len(str(max_val)) + 1
    loop_num = 1

    def _radix_sort(list):
        nonlocal iterations
        nonlocal loop_num

        while loop_num < iterations:
            output = []

            for num in list:
                q = num % (10 ** loop_num)
                queues[q].enqueue(num)

            for queue in queues:
                while queue.front:
                    output.append(queue.dequeue)

            loop_num += 1

            print(output)

            return _radix_sort(output)

        return list

    return _radix_sort(list)
