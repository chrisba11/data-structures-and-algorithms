from multi_bracket_validation import multi_bracket_validation
import pytest


def test_works_with_empty_string():
    string = ''
    assert multi_bracket_validation(string) is True


def test_works_with_curly_string():
    string = '{}'
    assert multi_bracket_validation(string) is True


def test_works_with_square_string():
    string = '[]'
    assert multi_bracket_validation(string) is True


def test_works_with_paren_string():
    string = '()'
    assert multi_bracket_validation(string) is True


def test_works_with_multi_string():
    string = '{[()]}'
    assert multi_bracket_validation(string) is True


def test_works_with_unmatched_string():
    string = '{[()]'
    assert multi_bracket_validation(string) is False
