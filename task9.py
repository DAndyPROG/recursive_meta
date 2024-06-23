class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class SingletonClass(metaclass=SingletonMeta):
    def __init__(self, value):
        self.value = value

singleton1 = SingletonClass(1)
singleton2 = SingletonClass(2)

print(singleton1 is singleton2) 
print(singleton1.value)  
print(singleton2.value) 
