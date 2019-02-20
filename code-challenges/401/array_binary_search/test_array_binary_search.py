from array_binary_search import binary_search


def test_with_odd_num_elem():
    actual = binary_search([1, 2, 4, 7, 9], 4)
    expected = 2
    assert actual == expected


def test_with_even_num_elem():
    actual = binary_search([1, 2, 4, 7], 7)
    expected = 3
    assert actual == expected


def test_with_no_matching_elem():
    actual = binary_search([1, 2, 4, 7, 9], 8)
    expected = -1
    assert actual == expected


def test_with_multiple_matches_both_mid():
    actual = binary_search([1, 4, 4, 5], 4)
    expected = 2
    assert actual == expected


def test_with_multiple_matches_both_less_than_mid():
    actual = binary_search([1, 2, 3, 4, 4, 5, 6, 7, 7, 8], 4)
    expected = 3
    assert actual == expected


def test_with_strings():
    actual = binary_search(['at', 'from', 'hello', 'hi', 'there', 'this'], 'hello')
    expected = 2
    assert actual == expected
