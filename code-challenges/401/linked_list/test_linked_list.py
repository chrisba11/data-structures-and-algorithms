from linked_list import LinkedList


def test_exists():
    """
    Does class LinkedList exist?
    """
    assert LinkedList


def test_empty():
    """
    Can successfully instantiate an empty linked list
    """
    assert LinkedList()


def test_insert_one():
    """
    Can properly insert one item into the linked list
    The head property will properly point to the first node in the linked list
    """
    courses = LinkedList()
    courses.insert('Code 201')

    assert courses.head.data == 'Code 201'


def test_insert_two():
    """
    Can properly insert multiple nodes into the linked list
    """
    courses = LinkedList()
    courses.insert('Code 301')
    courses.insert('Code 201')

    assert courses.head.data == 'Code 201'
    assert courses.head._next.data == 'Code 301'


def test_includes():
    """
    Will return true when finding a value within the linked list that exists
    """
    courses = LinkedList()
    courses.insert('Code 201')
    courses.insert('Code 301')
    courses.insert('Code 401: Python')

    assert courses.includes('Code 301')


def test_not_inlude():
    """
    Will return false when searching for a value in the linked list that does not exist
    """
    courses = LinkedList()
    courses.insert('Code 201')
    courses.insert('Code 301')
    courses.insert('Code 401: Python')

    assert not courses.includes('Code 101')


def test_print():
    """
    Can properly return a collection of all the values that exist in the linked list
    """
    courses = LinkedList()
    courses.insert('Code 401: Python')
    courses.insert('Code 301')
    courses.insert('Code 201')
    courses.insert('Code 102')
    courses.insert('Code 101')

    assert courses.print() == 'Code 101, Code 102, Code 201, Code 301, Code 401: Python'


def test_append():
    """

    """
    courses = LinkedList()
    courses.insert('Code 201')
    courses.insert('Code 102')
    courses.insert('Code 101')
    courses.append('Code 301')

    assert courses.print() == 'Code 101, Code 102, Code 201, Code 301'


def test_add_before():
    """

    """
    courses = LinkedList()
    courses.append('Code 101')
    courses.append('Code 102')
    courses.append('Code 201')
    courses.append('Code 401: Python')
    courses.add_before('Code 401: Python', 'Code 301')

    assert courses.print() == 'Code 101, Code 102, Code 201, Code 301, Code 401: Python'


def test_add_before_first():
    """

    """
    courses = LinkedList()
    courses.append('Code 101')
    courses.append('Code 102')
    courses.append('Code 201')
    courses.append('Code 401: Python')
    courses.add_before('Code 101', 'Code 301')

    assert courses.print() == 'Code 301, Code 101, Code 102, Code 201, Code 401: Python'


def test_add_after():
    """

    """
    courses = LinkedList()
    courses.append('Code 101')
    courses.append('Code 102')
    courses.append('Code 201')
    courses.append('Code 401: Python')
    courses.add_after('Code 201', 'Code 301')

    assert courses.print() == 'Code 101, Code 102, Code 201, Code 301, Code 401: Python'


def test_add_after_last():
    """

    """
    courses = LinkedList()
    courses.append('Code 101')
    courses.append('Code 102')
    courses.append('Code 201')
    courses.append('Code 401: Python')
    courses.add_after('Code 401: Python', 'Code 301')

    assert courses.print() == 'Code 101, Code 102, Code 201, Code 401: Python, Code 301'


def test_0_from_end():
    """

    """
    courses = LinkedList()
    courses.append('Code 101')
    courses.append('Code 102')
    courses.append('Code 201')
    courses.append('Code 301')
    courses.append('Code 401: Python')

    assert k_from_end(courses, 0) == 'Code 401: Python'


def test_2_from_end():
    """

    """
    courses = LinkedList()
    courses.append('Code 101')
    courses.append('Code 102')
    courses.append('Code 201')
    courses.append('Code 301')
    courses.append('Code 401: Python')

    assert k_from_end(courses, 2) == 'Code 301'


def test_6_from_end():
    """

    """
    courses = LinkedList()
    courses.append('Code 101')
    courses.append('Code 102')
    courses.append('Code 201')
    courses.append('Code 301')
    courses.append('Code 401: Python')

    assert k_from_end(courses, 6) == Exception
