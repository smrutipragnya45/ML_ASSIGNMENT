# Create a private attribute in a class and access it using a method.
class MyClass:
    def __init__(self):
        self.__private_attr = "I am private"

    def get_private_attr(self):
        return self.__private_attr

obj = MyClass()
print(obj.get_private_attr())