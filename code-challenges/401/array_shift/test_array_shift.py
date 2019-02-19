from array_shift import insert_shift_array


def test_works_with_all_numbers():
    actual = insert_shift_array([1, 2, 3, 4, 5], 6)
    expected = [1, 2, 3, 6, 4, 5]
    assert actual == expected


def test_works_with_strings_and_numbers():
    actual = insert_shift_array(['A', 2, 3, 'Steve', 5], 'Tony')
    expected = ['A', 2, 3, 'Tony', 'Steve', 5]
    assert actual == expected


def test_works_with_all_empty_strings():
    actual = insert_shift_array(['', '', '', ''], '')
    expected = ['', '', '', '', '']
    assert actual == expected

