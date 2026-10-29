class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Return value at index i
    def get(self, i):
        if i < 0:
            return -1

        current = self.head
        index = 0

        while current:
            if index == i:
                return current.val

            current = current.next
            index += 1

        return -1

    # Insert node at the beginning
    def insertHead(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    # Insert node at the end
    def insertTail(self, val):
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node

    # Remove node at index i
    def remove(self, i):
        if i < 0 or self.head is None:
            return False

        if i == 0:
            self.head = self.head.next
            return True

        current = self.head
        index = 0

        while current.next:
            if index + 1 == i:
                current.next = current.next.next
                return True

            current = current.next
            index += 1

        return False

    # Return all values as a Python list
    def getValues(self):
        values = []
        current = self.head

        while current:
            values.append(current.val)
            current = current.next

        return values


# Main function
if __name__ == "__main__":
    ll = LinkedList()

    ll.insertHead(20)
    ll.insertHead(10)
    ll.insertTail(30)
    ll.insertTail(40)

    print("Linked List:", ll.getValues())
    print("Value at index 2:", ll.get(2))

    ll.remove(1)
    print("After removing index 1:", ll.getValues())

    print("Value at index 1:", ll.get(1))
    print("Remove index 10:", ll.remove(10))