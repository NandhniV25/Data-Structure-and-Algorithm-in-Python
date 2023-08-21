days = input("How many day's temperature? ")
my_temp = list()
for x in range(int(days)):
    each = input(f"Day {x+1}'s high temperature: ")
    my_temp.append(int(each))
avg = sum(my_temp)/len(my_temp)
print("Average = ", avg)
count = 0
for x in my_temp:
    if x > avg:
        count += 1
print(f"{count} day(s) above average")

#Below code is not suitable bcz it doesn't store the user input so you can use array or list
numDays = int(input("How many day's temperature? "))
total = 0 
for i in range(1, numDays+1):
    nextDay = int(input(f"Day {i}'s high temperature: "))
    total += nextDay
avg = round(total/numDays, 2)
print("\nAverage = ", avg)
