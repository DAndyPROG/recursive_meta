class MyMeta(type):
    def __new__(cls, name, bases, class_dict):
        print(f"Creating class {name}")
        return super().__new__(cls, name, bases, class_dict)

class MyClass(metaclass=MyMeta):
    pass

class AnotherClass(metaclass=MyMeta):
    def __init__(self):
        print("AnotherClass instance created")

my_instance = MyClass()
another_instance = AnotherClass()
