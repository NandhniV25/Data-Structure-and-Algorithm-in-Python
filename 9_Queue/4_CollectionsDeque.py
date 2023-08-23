from collections import deque

customQueue = deque(maxlen=3)
print(customQueue)

customQueue.append(1)
customQueue.append(2)
customQueue.append(3)
print(customQueue)

customQueue.append(4)
# override the first element. 
#careful about this. 
#Act as a circular Q but it does n't throw exceptions
print(customQueue) 

print(customQueue.popleft())
print(customQueue)

print(customQueue.clear())
print(customQueue)