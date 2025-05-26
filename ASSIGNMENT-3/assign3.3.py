# Create a class with a class variable and instance variable.
class Sample:
    class_variable = "I am a class variable"

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable

obj = Sample("I am an instance variable")
print(Sample.class_variable)
print(obj.instance_variable)