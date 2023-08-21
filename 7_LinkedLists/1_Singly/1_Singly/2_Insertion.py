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
    
    # Printing the linkedlist
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result
        
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
        
    # Insertion at the beginning
    # Time = O(1) and Space = O(1)
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        
    # Insertion based on the index
    # Time = O(N) and Space = O(1)
    def insert(self, index, value):
        new_node = Node(value)
        if index < 0 or index > self.length:
            return False
        elif self.head is None or self.length == 0:
            self.head = new_node
            self.tail = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            temp_node = self.head
            for _ in range(index-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next 
            temp_node.next = new_node
        self.length += 1
        return True
        
newLinkedList = LinkedList()
newLinkedList.append(10)
newLinkedList.append(20)
newLinkedList.append(30)
print(newLinkedList.length)
print(newLinkedList.head.value)
print(newLinkedList)
newLinkedList.prepend(40)
newLinkedList.prepend(50)
newLinkedList.prepend(60)
print(newLinkedList.length)
print(newLinkedList.head.value)
print(newLinkedList)
newLinkedList.insert(3, 70)
print(newLinkedList.length)
print(newLinkedList.head.value)
print(newLinkedList)

