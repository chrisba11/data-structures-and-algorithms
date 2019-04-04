from .radix_sort import radix_sort
import pytest


def test_sorted_array_returns_same_sorted_array():
    sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert radix_sort(sorted_list) == sorted_list


def test_backward_sorted_array_returns_sorted_array():
    sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    backward_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert radix_sort(backward_list) == sorted_list


def test_mixed_array_returns_sorted_array():
    sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    mixed_list = [7, 5, 2, 4, 3, 8, 9, 10, 1, 6]
    assert radix_sort(mixed_list) == sorted_list


def test_mixed_array_returns_sorted_array_larger_nums():
    sorted_list = [4, 17, 28, 107, 123, 150, 309, 754, 1074, 20652]
    mixed_list = [20652, 17, 4, 150, 123, 1074, 309, 28, 754, 107]
    assert radix_sort(mixed_list) == sorted_list


def test_empty_array():
    assert radix_sort([]) == []


def test_single_element_array():
    assert radix_sort([1]) == [1]
