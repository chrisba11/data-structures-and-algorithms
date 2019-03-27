from .left_join import left_join


def test_exists():
    assert left_join


def test_matching_tables(ht1, ht2):
    dict = {
        'A': ['Z', 'Z'],
        'B': ['Y', 'Y'],
        'C': ['X', 'X'],
        'D': ['W', 'W'],
    }
    assert left_join(ht1, ht2) == dict


def test_matching_tables_with_collisions_at_same_key(ht1, ht4):
    dict = {
        'A': ['Z', 'Z | $'],
        'B': ['Y', 'Y'],
        'C': ['X', 'X'],
        'D': ['W', 'W'],
    }
    assert left_join(ht1, ht4) == dict


def test_tables_not_matching_any_keys(ht1, ht3):
    dict = {
        'A': ['Z', None],
        'B': ['Y', None],
        'C': ['X', None],
        'D': ['W', None],
    }
    assert left_join(ht1, ht3) == dict
