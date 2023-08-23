class Stack:
    def __init__(self):
        self.list = []
    
    def __str__(self):
        values = reversed(self.list)
        values = [str(x) for x in values]
        return '\n'.join(values)
    
    # isEmpty
    # Time = O(1) and Space = O(1)
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
    # push
    # Time = O(N) and Space = O(1)
    def push(self, value):
        self.list.append(value)
        return "The element has been successfully inserted"

    # pop
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
    
    # delete
    #  Time = O(1) and Space = O(1)
    def delete(self):
        self.list = None




customStack = Stack()
print(customStack.isEmpty())
customStack.push(1)
customStack.push(2)
print("Top of the stack",customStack.peek())
customStack.push(3)
print("Top of the stack",customStack.peek())
print("Elements in the Stack :")
print(customStack)
print(customStack.pop())
print("Top of the stack",customStack.peek())