class RenamePrivateMeta(type):
    def __new__(cls, name, bases, class_dict):
        new_class_dict = {}
        for attr_name, attr_value in class_dict.items():
            if attr_name.startswith('__') and not attr_name.endswith('__'):
                new_attr_name = f'__private_{attr_name.lstrip("_")}'
                new_class_dict[new_attr_name] = attr_value
            else:
                new_class_dict[attr_name] = attr_value
        return super().__new__(cls, name, bases, new_class_dict)

class MyClass(metaclass=RenamePrivateMeta):
    __secret = "I am secret"
    def __init__(self):
        self.__hidden = "I am hidden"

    def __private_method(self):
        return "This is a private method"

print(hasattr(MyClass, '__private_secret')) 
print(hasattr(MyClass, '__secret'))         

instance = MyClass()
print(hasattr(instance, '__private_hidden'))  
print(hasattr(instance, '__hidden'))        

print(instance._MyClass__private_method()) 
