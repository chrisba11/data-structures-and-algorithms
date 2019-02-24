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
    courses.insert('Code 201')
    courses.insert('Code 301')

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
    courses.insert('Code 101')
    courses.insert('Code 102')
    courses.insert('Code 201')
    courses.insert('Code 301')
    courses.insert('Code 401: Python')

    assert courses.print() == 'Code 101, Code 102, Code 201, Code 301, Code 401: Python'
