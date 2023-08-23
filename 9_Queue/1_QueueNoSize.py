class Queue:
    def __init__(self):
        self.items = []
    
    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)
    
    #  Time = O(1) and Space = O(1)
    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False
    
    #  Time = O(N)amortized constant and Space = O(1)
    def enqueue(self, value):
        self.items.append(value)
        return "The element is inserted at the end of Queue"
    
    #  Time = O(N)(shifting one position to the left) and Space = O(1) 
    def dequeue(self):
        if self.isEmpty():
            return "The is not any element in the Queue"
        else:
            return self.items.pop(0)
    
    #  Time = O(1) and Space = O(1)
    def peek(self):
        if self.isEmpty():
            return "The is not any element in the Queue"
        else:
            return self.items[0]
    
    #  Time = O(1) and Space = O(1)
    def delete(self):
        self.items = None

customQueue = Queue()
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
print("Top of the Queue",customQueue.peek())
print("Elements in the Queue :")
print(customQueue)
print(customQueue.dequeue())
print("Top of the Queue",customQueue.peek())
print("Elements in the Queue :")
print(customQueue)
customQueue.delete()
