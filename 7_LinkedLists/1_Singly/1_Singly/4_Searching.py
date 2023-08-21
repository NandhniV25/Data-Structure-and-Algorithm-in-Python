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
    
    # Searching of singly linkedlist
    # Time = O(N) and Space = O(1)
    def search(self, target):
        current = self.head
        while current: # while current is not None: 
            if current.value == target:
                return True
            current = current.next
        return False
    
    # Searching of singly linkedlist return index value
    # Time = O(N) and Space = O(1)
    def searchIndex(self, target):
        current = self.head
        index = 0
        while current: # while current is not None: 
            if current.value == target:
                return index
            current = current.next
            index += 1
        return -1

newLinkedList = LinkedList()
newLinkedList.append(10)
newLinkedList.append(20)
newLinkedList.append(30)
print(newLinkedList.search(80))
print(newLinkedList.searchIndex(30))