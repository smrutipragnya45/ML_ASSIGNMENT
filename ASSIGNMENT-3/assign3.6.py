# Create two objects of a class and demonstrate that they are independent.
class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        
counter1 = Counter()
counter2 = Counter()

counter1.increment()
print(f"Counter1: {counter1.count}")
print(f"Counter2: {counter2.count}")