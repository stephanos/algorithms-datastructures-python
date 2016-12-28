from linked_list import LinkedList


def test_empty_list():
    linked_list = LinkedList()
    assert linked_list.size() == 0

def test_append():
    linked_list = LinkedList()

    linked_list.append('Alice')
    assert linked_list.size() == 1
    assert linked_list.first.value == 'Alice'
    assert linked_list.first.prev_node is None
    assert linked_list.first.next_node is None
    assert linked_list.last.value == 'Alice'
    assert linked_list.last.prev_node is None
    assert linked_list.last.next_node is None

    linked_list.append('Bob')
    assert linked_list.size() == 2
    assert linked_list.first.value == 'Alice'
    assert linked_list.first.next_node is not None
    assert linked_list.first.prev_node is None
    assert linked_list.last.value == 'Bob'
    assert linked_list.last.prev_node is linked_list.first
    assert linked_list.last.next_node is None

    linked_list.append('Chris')
    assert linked_list.size() == 3
    assert linked_list.first.value == 'Alice'
    assert linked_list.first.next_node is not None
    assert linked_list.first.prev_node is None
    assert linked_list.last.value == 'Chris'
    assert linked_list.last.next_node is None
    assert linked_list.last.prev_node.value == 'Bob'

def test_prepend():
    linked_list = LinkedList()

    linked_list.prepend('Chris')
    assert linked_list.size() == 1
    assert linked_list.first.value == 'Chris'
    assert linked_list.first.next_node is None
    assert linked_list.last.value == 'Chris'
    assert linked_list.last.next_node is None

    linked_list.prepend('Bob')
    assert linked_list.size() == 2
    assert linked_list.first.value == 'Bob'
    assert linked_list.first.next_node is linked_list.last
    assert linked_list.last.value == 'Chris'
    assert linked_list.last.next_node is None

    linked_list.prepend('Alice')
    assert linked_list.size() == 3
    assert linked_list.first.value == 'Alice'
    assert linked_list.first.next_node.value == 'Bob'
    assert linked_list.last.value == 'Chris'
    assert linked_list.last.next_node is None

def test_str():
    linked_list = LinkedList()
    assert linked_list.__str__() == 'LinkedList []'

    linked_list.append('Alice')
    linked_list.append('Bob')
    assert linked_list.__str__() == """LinkedList [
    Alice
    Bob
]"""
