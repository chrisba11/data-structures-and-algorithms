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


def test_add_one():
    ht = Hashtable()
    ht.add('test', 'object')
    assert ht._array[ht.hash('test')].head.data == ('test', 'object')


def test_add_two_to_same_index():
    ht = Hashtable()
    ht.add('test', 'object')
    ht.add('test', 'array')
    assert ht._array[ht.hash('test')].head.data == ('test', 'array')
    assert ht._array[ht.hash('test')].head._next.data == ('test', 'object')


def test_hash_is_same_each_time():
    ht = Hashtable()
    assert ht.hash('test') == ht.hash('test')
