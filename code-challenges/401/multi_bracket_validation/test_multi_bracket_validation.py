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


def test_works_with_unmatched_string_1():
    string = '{[()]'
    assert multi_bracket_validation(string) is False


def test_works_with_unmatched_string_2():
    string = '{abcdefg hijklmnop'
    assert multi_bracket_validation(string) is False


def test_works_with_unmatched_string_3():
    string = '[]('
    assert multi_bracket_validation(string) is False


def test_works_with_unmatched_string_4():
    string = '[[{('
    assert multi_bracket_validation(string) is False


def test_works_with_matched_string_1():
    string = '{this is a story of a lovely [lady]}'
    assert multi_bracket_validation(string) is True


def test_works_with_matched_string_2():
    string = 'This does not have brackets'
    assert multi_bracket_validation(string) is True
