import pytest
from ..hashtable.hashtable import Hashtable


@pytest.fixture
def ht1():
    ht1 = Hashtable()
    ht1.add('A', 'Z')
    ht1.add('B', 'Y')
    ht1.add('C', 'X')
    ht1.add('D', 'W')
    return ht1


@pytest.fixture
def ht2():
    ht2 = Hashtable()
    ht2.add('A', 'Z')
    ht2.add('B', 'Y')
    ht2.add('C', 'X')
    ht2.add('D', 'W')
    return ht2


@pytest.fixture
def ht3():
    ht3 = Hashtable()
    ht3.add('1', 'AA')
    ht3.add('2', 'BB')
    ht3.add('3', 'CC')
    ht3.add('4', 'DD')
    return ht3


@pytest.fixture
def ht4():
    ht4 = Hashtable()
    ht4.add('A', 'Z')
    ht4.add('B', 'Y')
    ht4.add('C', 'X')
    ht4.add('D', 'W')
    ht4.add('A', '$')
    return ht4
