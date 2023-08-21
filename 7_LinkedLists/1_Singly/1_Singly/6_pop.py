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
    
    # pop the first element of singly linkedlist
    # Time = O(1) and Space = O(1)
    def pop_first(self):
        if self.length == 0:
            return None
        popped_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            popped_node.next = None
        self.length -= 1
        return popped_node
    
    # pop removes the last element of singly linkedlist. return value
    # Time = O(N) and Space = O(1)
    def pop(self):
        if self.length == 0:
            return None
        popped_node = self.tail
        if self.length == 1:
            self.head = self.tail = None
        else:
            temp = self.head
            while temp.next is not self.tail:
                temp = temp.next
            temp.next = None
            self.tail = temp
        self.length -= 1
        return popped_node
    
newLinkedList = LinkedList()
newLinkedList.append(10)
newLinkedList.append(20)
newLinkedList.append(30)
print(newLinkedList.pop_first())
print(newLinkedList.pop())