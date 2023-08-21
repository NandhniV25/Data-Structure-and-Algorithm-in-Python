class StarCookie:
    milk = 0.1 # like global variable. obj can access the variable   
    def __init__(self, color, weight):
        self.color = color
        self.weight = weight
        
starCookie1 = StarCookie("Red", 15)
print(starCookie1.color)
print(starCookie1.weight)

starCookie2 = StarCookie("Green", 16)
print(starCookie2.color)
print(starCookie2.weight)

print(starCookie1.milk)
print(starCookie2.milk)
print(StarCookie.milk)

# Dictionary
print(starCookie1.__dict__)
print(starCookie2.__dict__)
print(StarCookie.__dict__)

starCookie2.milk = 0.2

print(starCookie1.milk)
print(starCookie2.milk)
print(StarCookie.milk)

print(starCookie1.__dict__)
print(starCookie2.__dict__)
print(StarCookie.__dict__)