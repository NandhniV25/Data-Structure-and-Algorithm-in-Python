class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
    # Time = O(1) and Space = O(1)
        self.head = None
        self.tail = None
        self.length = 0
        
    # Insertion at the end
    # Time = O(1) and Space = O(1)
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    
    # Traversal of singly linkedlist
    # Time = O(N) and Space = O(1)
    def traverse(self):
        current = self.head
        while current is not None: # or while current:
            print(current.value, end = " ")
            current = current.next

newLinkedList = LinkedList()
newLinkedList.append(10)
newLinkedList.append(20)
newLinkedList.append(30)
newLinkedList.traverse()
