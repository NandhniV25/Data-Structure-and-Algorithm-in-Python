class YouTube:
    def __init__(self, userName, subscribers = 0, subscriptions = 0):
        self.userName = userName
        self.subscribers = subscribers
        self.subscriptions = subscriptions
        
    def subscribe(self, user):
        user.subscribers += 1
        self.subscriptions += 1

user1 = YouTube("Nandhni")
user2 = YouTube("Venkat")

user1.subscribe(user2)

print(f"User 1 Subscribers: {user1.subscribers}")
print(f"User 1 Subscriptions: {user1.subscriptions}")
print(f"User 2 Subscribers: {user2.subscribers}")
print(f"User 2 Subscriptions: {user2.subscriptions}")