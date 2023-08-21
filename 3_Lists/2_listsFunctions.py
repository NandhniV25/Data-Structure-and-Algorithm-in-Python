# List operations / functions
# + => Concatenation
# * => any element in the list can be repeative
a = [1,2,3]
b = [4,5,6]
c = a + b
print(c)
d = [0,1] * 4
print(d)
print(len(a),max(a),min(a),sum(a))

# List operations / functions
total = 0 
count = 0
while (True):
    inp = input('Enter a number: ') 
    if inp == 'done': break
    value = float(inp)
    total = total + value
    count = count + 1 
average = total / count			
print('Average:', average)

# Minimalize the above code
numlist = list() 
while (True):
    inp = input('Enter a number: ') 
    if inp == 'done': break
    value = float(inp)
    numlist.append(value)		
avg = sum(numlist) / len(numlist) 
print('Average:', avg)
