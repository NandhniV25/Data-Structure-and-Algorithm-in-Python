class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    
    #  Creation of Doubly Linked List
    #  Time = O(1) and Space = O(1)        
    def createDLL(self, nodeValue):
        node = Node(nodeValue)
        node.prev = None
        node.next = None
        self.head = node
        self.tail = node
        return "The DLL is created Successfully"
    
doubyLL = DoublyLinkedList()
doubyLL.createDLL(5)

print([node.value for node in doubyLL]) 