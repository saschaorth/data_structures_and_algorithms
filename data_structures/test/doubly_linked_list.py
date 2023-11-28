from doubly_linked_list import DoublyLinkedList


def test_insert():
    lst = DoublyLinkedList('a')
    for value in ['b', 'c', 'd', 'e']:
        lst.append(value)

    lst.insert(3, 'z')
    assert lst.length == 6
    assert str(lst) == str(['a', 'b', 'c', 'z', 'd', 'e'])


def test_remove():
    lst = DoublyLinkedList('a')
    for value in ['b', 'c', 'd', 'e']:
        lst.append(value)

    lst.remove(3)
    assert lst.length == 4
    assert str(lst) == str(['a', 'b', 'c', 'e'])
