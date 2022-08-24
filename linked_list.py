

class LinkedList:

    class Node:
        def __init__(self, data, next=None):
            self.data = data
            self.next = next

    def __init__(self):
        self.head = None

    def insert(self, data, index=0):
        node = self.Node(data, self.head)
        # First time, add end
        if self.head is None and index == -1:
            self.head = node
            return
        # Add start
        if index == 0:
            self.head = node
            return
        # Add at position
        else:
            if index == -1:
                node = self.Node(data, None)
                iteration = self.head
                while iteration.next:
                    iteration = iteration.next
                iteration.next = node
                return
            else:
                count = 0
                iteration = self.head
                while iteration.next:
                    count += 1
                    if count == index:
                        node = self.Node(data, iteration.next)
                        iteration.next = node
                        return
                    iteration = iteration.next

    def __len__(self):
        counter = 0
        iteration = self.head
        while iteration:
            counter += 1
            iteration = iteration.next
        return counter

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
    linked_list.insert(1, index=-1)
    linked_list.insert(3)
    linked_list.insert(7, index=-1)
    linked_list.insert(10, index=3)
    print('Length:', len(linked_list))
    print(linked_list)
