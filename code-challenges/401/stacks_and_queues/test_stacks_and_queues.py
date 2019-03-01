from stacks_and_queues import LinkedList, Node, Stack


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


def test_queue_enqueue():
    
