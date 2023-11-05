
class Node:
    def __init__(self, data):
        self.next = None
        self.data = data
        return


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        return

    def push(self, value):
        if not isinstance(value, Node):
            value = Node(value)

        if self.head is None:
            self.head = value
        else:
            self.tail.next = value

        self.tail = value

        return

    def get(self, index):
        if index < 0:
            return None

        current = self.head
        for i in range(index):
            if current is None:
                return None
            current = current.next

        if current is None:
            return None

        return current.data

    def remove(self, index):
        curr_index = 1
        curr_node = self.head
        prev_node = None

        while curr_node is not None:
            if curr_index == index:
                if prev_node is not None:
                    prev_node.next = curr_node.next
                else:
                    self.head = curr_node.next
                    return

            prev_node = curr_node
            curr_node = curr_node.next
            curr_index = curr_index + 1

        return

    def insert(self, index, value):
        if index < 0:
            return

        if index == 0:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node
            return

        curr = self.head
        for i in range(index-1):
            if curr is None:
                return
            curr = curr.next

        if curr is None:
            return

        new_node = Node(value)
        new_node.next = curr.next
        curr.next = new_node

