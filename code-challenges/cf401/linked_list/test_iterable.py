from .linked_list import LinkedList
import pytest


def test_linked_list_class():
    assert LinkedList


def test_linked_list_instance():
    assert LinkedList('foo')


def test_linked_list_add_one():
    ll = LinkedList()
    ll.append('apples')
    assert ll.head.data == 'apples'


def test_linked_list_add_two():
    ll = LinkedList()
    ll.append('apples')
    ll.append('bananas')
    assert ll.head.data == 'apples'
    assert ll.head.nxt.data == 'bananas'


def test_linked_list_iteration():
    ll = LinkedList()
    ll.append('apples')
    ll.append('bananas')

    items = []
    for item in ll:
        items.append(item)

    assert items == ['apples', 'bananas']


def test_linked_list_conversion():
    ll = LinkedList()
    ll.append('apples')
    ll.append('bananas')

    items = list(ll)

    assert items == ['apples', 'bananas']


def test_linked_list_expressesion():
    ll = LinkedList()
    ll.append('apples')
    ll.append('bananas')

    cap_fruits = [f.upper() for f in ll]

    assert cap_fruits == ['APPLES', 'BANANAS']


def test_linked_list_filter():
    letters = LinkedList()
    letters.append('a')
    letters.append('b')
    letters.append('c')
    letters.append('d')
    letters.append('e')
    letters.append('f')
    letters.append('g')

    vowels = 'aeiou'

    consonants = [char for char in letters if char not in vowels]

    assert consonants == ['b', 'c', 'd', 'f', 'g']


def test_append_operator():
    animals = LinkedList()

    animals += 'giraffe'

    assert list(animals) == ['giraffe']


@pytest.mark.skip
def test_concat():
    montagues = LinkedList(['Romeo', 'Benvolio'])

    capulets = LinkedList(['Juliet', 'Tybalt'])

    tutti = montagues + capulets

    assert len(list(tutti)) == 4

    assert len(list(montagues)) == 2
