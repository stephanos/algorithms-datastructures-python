class Node():
    def __init__(self, value=None, prev_node=None, next_node=None):
        self.value = value
        self.prev_node = prev_node
        self.next_node = next_node


class LinkedList():

    def __init__(self):
        self.first = None
        self.last = None

    def size(self):
        current = self.first
        count = 0
        while current:
            count += 1
            current = current.next_node
        return count

    def append(self, value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        elif self.last == self.first:
            self.last = new_node
            new_node.prev_node = self.first
            self.first.next_node = new_node
        else:
            self.last.next_node = new_node
            new_node.prev_node = self.last
            self.last = new_node

    def prepend(self, value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        elif self.last == self.first:
            self.first = new_node
            self.first.next_node = self.last
            self.last.prev_node = self.first
        else:
            new_node.next_node = self.first
            self.first.prev_node = new_node
            self.first = new_node

    def __str__(self):
        if self.first != None:
            current = self.first
            out = 'LinkedList [\n'
            while current:
                out += '    {}\n'.format(current.value)
                current = current.next_node
            return out + ']'
        return 'LinkedList []'
