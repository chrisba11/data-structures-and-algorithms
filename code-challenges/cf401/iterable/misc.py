from ..hashtable.hashtable import Hashtable


def has_dupes(val):
    ht = Hashtable()
    if hasattr(val, '__iter__'):
        for i in val:
            if ht.contains(val):
                print(val)
                return True
            ht.add(val, val)
        return False
    return False
