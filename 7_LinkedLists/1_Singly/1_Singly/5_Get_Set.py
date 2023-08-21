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
    
    # Get method of singly linkedlist
    # Time = O(N) and Space = O(1)
    def get(self, index):
        if index == -1:
            return self.tail
        if index < -1 or index >= self.length:
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        return current
    
    # Set method of singly linkedlist
    # Time = O(N) and Space = O(1)
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

newLinkedList = LinkedList()
newLinkedList.append(10)
newLinkedList.append(20)
newLinkedList.append(30)
print(newLinkedList.get(2))
print(newLinkedList.get(-1))
print(newLinkedList.set_value(2, 50))