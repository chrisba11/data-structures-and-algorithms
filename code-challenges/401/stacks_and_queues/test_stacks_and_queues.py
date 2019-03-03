from stacks_and_queues import Node, Stack, Queue


def test_stack_push_one():
    hats = Stack()
    hats.push('seahawks')

    assert hats.top.data == 'seahawks'


def test_stack_push_two():
    hats = Stack()
    hats.push('seahawks')
    hats.push('gray')

    assert hats.top.data == 'gray'


def test_stack_push_two_return_first_value():
    hats = Stack()
    hats.push('seahawks')
    hats.push('gray')

    assert hats.top._next.data == 'seahawks'


def test_stack_pop_one():
    hats = Stack()
    hats.push('seahawks')
    hats.push('gray')
    hats.push('tan')
    hats.push('black')
    hats.pop()

    assert hats.top.data == 'tan'


def test_stack_pop_three():
    hats = Stack()
    hats.push('seahawks')
    hats.push('gray')
    hats.push('tan')
    hats.push('black')
    hats.pop()
    hats.pop()
    hats.pop()

    assert hats.top.data == 'seahawks'


def test_stack_pop_return_value():
    hats = Stack()
    hats.push('seahawks')
    hats.push('gray')

    assert hats.pop() == 'gray'


def test_stack_pop_all_return():
    hats = Stack()
    hats.push('gray')
    hats.pop()

    assert hats.pop() == 'Empty Stack'


def test_stack_pop_all_top():
    hats = Stack()
    hats.push('seahawks')
    hats.push('gray')
    hats.pop()
    hats.pop()

    assert hats.top is None


def test_stack_peek():
    hats = Stack()
    hats.push('seahawks')
    hats.push('gray')
    hats.push('tan')
    hats.push('black')

    assert hats.peek() == 'black'


def test_stack_peek_empty():
    hats = Stack()

    assert hats.peek() == 'Empty Stack'


def test_queue_enqueue_one_front():
    line = Queue()
    line.enqueue('Steve')

    assert line.front.data == 'Steve'


def test_queue_enqueue_one_rear():
    line = Queue()
    line.enqueue('Steve')

    assert line.rear.data == 'Steve'


def test_queue_dequeue_return():
    line = Queue()
    line.enqueue('Steve')

    assert line.dequeue() == 'Steve'


def test_queue_dequeue_new_front():
    line = Queue()
    line.enqueue('Steve')
    line.enqueue('Ted')
    line.enqueue('Mary')
    line.enqueue('Pam')
    line.dequeue()

    assert line.front.data == 'Ted'


def test_queue_dequeue_multiple():
    line = Queue()
    line.enqueue('Steve')
    line.enqueue('Ted')
    line.enqueue('Mary')
    line.enqueue('Pam')
    line.dequeue()
    line.dequeue()
    line.dequeue()

    assert line.front.data == 'Pam'


def test_queue_dequeue_empty():
    line = Queue()

    assert line.dequeue() == 'Empty Queue'


def test_queue_peek():
    line = Queue()
    line.enqueue('Steve')
    line.enqueue('Ted')
    line.enqueue('Mary')
    line.enqueue('Pam')

    assert line.peek() == 'Steve'


def test_queue_peek_empty():
    line = Queue()

    assert line.peek() == 'Empty Queue'
