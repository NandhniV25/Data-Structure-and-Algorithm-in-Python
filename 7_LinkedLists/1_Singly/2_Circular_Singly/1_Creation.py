
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    
    def remove_duplicates(self):
        setElements = set()
        current = self.head.next 
        prev = self.head
        while current.next:
            if current.value not in setElements:
                setElements.add(current.value)
                prev = current
                current = current.next
            else:
                temp = current
                prev.next = current.next
                prev = current.next
                if prev.next:
                    return 
                current = current.next.next
                
                temp.next = None
        self.tail=current
        
                
list1 = LinkedList()
list1.append(1)
list1.append(2)
list1.append(4)
list1.append(3)
list1.append(2)
print(list1)
print(list1.remove_duplicates())
print(list1)