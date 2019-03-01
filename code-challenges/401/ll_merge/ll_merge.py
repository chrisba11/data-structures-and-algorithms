from linked_list import LinkedList as ll


def merge_lists(linked_list_1, linked_list_2):
    """

    """
    list_one_len = 0
    list_two_len = 0

    try:
        if linked_list_1.head:
            current_1 = linked_list_1.head
    except:
        return linked_list_2

    try:
        if linked_list_2.head:
            current_2 = linked_list_2.head
    except:
        return linked_list_1

    while current_1._next:
        list_one_len += 1

    while current_2._next:
        list_two_len += 1

    current_1 = linked_list_1.head
    current_2 = linked_list_2.head

    while i in range(list_one_len):
        if current_1 and current_2:
            ll.add_after(current_1, current_2)
            current_1 = current_1._next
            current_2 = current_2._next
        elif current_2 and not current_1:
            ll.add_before(current_1, current_2)
        else:
            return
