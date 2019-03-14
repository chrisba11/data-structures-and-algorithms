from hashtable import Hashtable


def test_Hashtable_exists():
    assert Hashtable


def test_add_exists():
    ht = Hashtable()
    assert ht.add


def test_get_exists():
    ht = Hashtable()
    assert ht.get


def test_contains_exists():
    ht = Hashtable()
    assert ht.contains


def test_hash_exists():
    ht = Hashtable()
    assert ht.hash


def test_has_array_of_1024():
    ht = Hashtable()
    assert len(ht._array) == 1024
