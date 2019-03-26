from repeated_word.repeated_word import repeated_word
from tree.tree import BinarySearchTree


def test_function_exists():
    assert repeated_word


def test_works_with_short_string():
    string = 'This string repeats the word string'
    assert repeated_word(string) == 'string'


def test_works_with_longer_string():
    string = 'This is a slightly longer string that will eventually have a repeat'
    assert repeated_word(string) == 'a'


def test_works_with_empty_string():
    string = ''
    assert repeated_word(string) is False


def test_works_with_single_word_string():
    string = 'The'
    assert repeated_word(string) is False
