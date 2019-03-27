def left_join(ht1, ht2):
    join_dict = {}

    for bucket in ht1._array:
        if bucket is not None:
            curr = bucket.head
            while curr:
                key = curr.data[0]
                val = curr.data[1]
                join_dict[key] = [val]
                curr = curr._next

    for key in join_dict:
        if ht2.contains(key):
            val = ht2.get(key)
            join_dict[key].append(val)
        else:
            join_dict[key].append(None)

    return join_dict
