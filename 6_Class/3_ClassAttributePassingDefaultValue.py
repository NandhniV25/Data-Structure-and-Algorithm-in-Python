class YouTube:
    def __init__(self, userName, subscribers = 0):
        self.userName = userName
        self.subscribers = subscribers

user1 = YouTube("Nandhni")
print(user1.userName)
print(user1.subscribers)

user2 = YouTube("Venkat")
print(user2.userName)
print(user2.subscribers)
user2.subscribers = 5
print(user2.subscribers)