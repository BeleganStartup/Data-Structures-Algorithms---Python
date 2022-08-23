

class LinkedList:

    class Node:
        def __init__(self, data, next=None):
            self.data = data
            self.next = next

    def __init__(self):
        self.head = None

    def start_insert(self, data):
        node = self.Node(data, self.head)
        self.head = node

    def end_insert(self, data):
        if self.head is None:
            self.start_insert(data)
            return
        node = self.Node(data, None)
        iteration = self.head
        while iteration.next:
            iteration = iteration.next
        iteration.next = node

    def __len__(self):
        count = 0
        if self.head is not None:
            iteration = self.head
            while iteration:
                count += 1
                iteration = iteration.next
        return count

    def __str__(self):
        if self.head is None:
            return '[]'
        iteration = self.head
        output = '['
        while iteration:
            output += iteration.data.__str__()
            iteration = iteration.next
            if iteration:
                output += ', '
        output += ']'
        return output


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.start_insert(1)
    linked_list.start_insert(3)
    linked_list.start_insert(7)
    linked_list.end_insert(10)
    print('Length:', len(linked_list))
    print(linked_list)
