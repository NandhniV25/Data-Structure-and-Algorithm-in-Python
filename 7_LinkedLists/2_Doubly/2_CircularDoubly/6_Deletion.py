class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break
    
    #  Creation of Circular Doubly Linked List
    #  Time = O(1) and Space = O(1)
    def createCDLL(self, nodeValue):
        newNode = Node(nodeValue)
        self.head = newNode
        self.tail = newNode
        newNode.prev = newNode
        newNode.next = newNode
        return "The CDLL is created successfully"
    
    # Insertion Method in Circular Doubly Linked List
    #  Time = O(N) and Space = O(1)
    def insertCDLL(self, value, location):
        if self.head is None:
            return "The CDLL does not exist"
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.head = newNode
                self.tail.next = newNode
            elif location == 1:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                newNode.next = tempNode.next
                newNode.prev = tempNode
                newNode.next.prev = newNode
                tempNode.next = newNode
            return "The node has been successfully inserted"
    
    # Delete a node from Circular Doubly Linked List
    #  Time = O(N) and Space = O(1)
    def deleteNode(self, location):
        if self.head is None:
            print("There is not any node to delete")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = self.tail
                    self.tail.next = self.head
            elif location == 1:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = self.head
                    self.head.prev = self.tail
            else:
                curNode = self.head
                index = 0
                while index < location - 1:
                    curNode = curNode.next
                    index += 1
                curNode.next = curNode.next.next
                curNode.next.prev = curNode
            print("The node has been successfully deleted")
    
    # Delete entire Circular Doubly Linked List
    #  Time = O(N) and Space = O(1)
    def deleteCDLL(self):
        if self.head is None:
            print("There is not any element to delete")
        else:
            self.tail.next = None
            tempNode = self.head
            while tempNode:
                tempNode.prev = None
                tempNode = tempNode.next
            self.head = None
            self.tail = None
            print("The CDLL has been successfully deleted")
            
circularDLL = CircularDoublyLinkedList()
circularDLL.createCDLL(5)
print([node.value for node in circularDLL])
circularDLL.insertCDLL(0,0)
circularDLL.insertCDLL(1,1)
circularDLL.insertCDLL(2,2)
circularDLL.insertCDLL(4,-1)
print([node.value for node in circularDLL])
print(circularDLL.deleteNode(2))
circularDLL.deleteCDLL()
print([node.value for node in circularDLL])