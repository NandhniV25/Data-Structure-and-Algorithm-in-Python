class Stack:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.list = []
    
    def __str__(self):
        values = reversed(self.list)
        values = [str(x) for x in values]
        return '\n'.join(values)
    
    # isEmpty
    #  Time = O(1) and Space = O(1)
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
    
    # isFull
    #  Time = O(1) and Space = O(1)
    def isFull(self):
        if len(self.list) == self.maxSize:
            return True
        else:
            return False
    
    #  Push
    #  Time = O(N) and Space = O(1)
    def push(self, value):
        if self.isFull():
            return "The stack is full"
        else:
            self.list.append(value)
            return "The element has been successfully inserted"
    # Pop
    #  Time = O(1) and Space = O(1)
    def pop(self):
        if self.isEmpty():
            return "There is not any element in the stack"
        else:
            return self.list.pop()
    
    # peek
    #  Time = O(1) and Space = O(1)
    def peek(self):
        if self.isEmpty():
            return "There is not any element in the stack"
        else:
            return self.list[len(self.list)-1]

    #  delete
    def delete(self):
        self.list = None
    

customStack = Stack(4)
print(customStack.isEmpty())
print(customStack.isFull())
customStack.push(1)
customStack.push(2)
customStack.push(3)
print("Top of the stack",customStack.peek())
customStack.push(5)
print("Top of the stack",customStack.peek())
print("Elements in the Stack :")
print(customStack)
print(customStack.pop())
print("Top of the stack",customStack.peek())