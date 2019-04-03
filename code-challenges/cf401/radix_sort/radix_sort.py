from ..stacks_and_queues.stacks_and_queues import Queue


def radix_sort(list):
    queues = [Queue() for i in range(10)]
    print(queues)
