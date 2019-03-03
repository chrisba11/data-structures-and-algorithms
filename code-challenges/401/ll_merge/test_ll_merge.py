from ll_merge import ll, merge_lists
from linked_list import Node
import pytest


def create_linked_lists():
    list_1 = ll()
    list_1.append('1')
    list_1.append('2')
    list_1.append('3')
    list_1.append('4')

    list_2 = ll()
    list_2.append('A')
    list_2.append('B')
    list_2.append('C')
    list_2.append('D')

    list_3 = ll()
    list_3.append('Y')
    list_3.append('Z')

    list_4 = ll()


def text_ll_merge_equal_length_lists():
    create_linked_lists()
    assert print(merge_lists(list_1, list_2)) == '1, A, 2, B, 3, C, 4, D'


def text_ll_merge_equal_length_lists(create_linked_lists):
    assert print(merge_lists(list_2, list_1)) == 'A, 1, B, 2, C, 3, D, 4'


def text_ll_merge_equal_length_lists(create_linked_lists):
    assert print(merge_lists(list_1, list_3)) == '1, Y, 2, Z, 3, 4'


def text_ll_merge_equal_length_lists(create_linked_lists):
    assert print(merge_lists(list_1, list_2)) == '1, 2, 3, 4'
