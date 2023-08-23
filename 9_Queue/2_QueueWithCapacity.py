class Queue:
    #  Time = O(1) and Space = O(N)
    def __init__(self, maxSize):
        self.items = maxSize * [None]
        self.maxSize = maxSize
        self.start = -1
        self.top = -1 
    
    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)
    
    #  Time = O(1) and Space = O(1)
    def isFull(self):
        if self.top + 1 == self.start:
            return True
        elif self.start == 0 and self.top + 1 == self.maxSize:
            return True
        else:
            return False
    
    #  Time = O(1) and Space = O(1)
    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False
    
    #  Time = O(1) and Space = O(1)
    def enqueue(self, value):
        if self.isFull():
            return "The queue is full"
        else:
            if self.top + 1 == self.maxSize:
                self.top = 0
            else:
                self.top += 1
                if self.start == -1:
                    self.start = 0
            self.items[self.top] = value
            return "The element is inserted at the end of Queue"
    
    #  Time = O(1) and Space = O(1)
    def dequeue(self):
        if self.isEmpty():
            return "There is not any element in the Queue"
        else:
            firstElement = self.items[self.start]
            start = self.start
            if self.start == self.top:
                self.start = -1
                self.top = -1
            elif self.start + 1 == self.maxSize:
                self.start = 0
            else:
                self.start += 1
            self.items[start] = None
            return firstElement
    
    #  Time = O(1) and Space = O(1)
    def peek(self):
        if self.isEmpty():
            return "There is not any element in the Queue"
        else:
            return self.items[self.start]
    
    #  Time = O(1) and Space = O(1)
    def delete(self):
        self.items = self.maxSize * [None]
        self.top = -1
        self.start = -1

customQueue = Queue(4)
print(customQueue.isEmpty())
print(customQueue.isFull())
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