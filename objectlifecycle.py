# use of __del__

class MyClass:
    def __init__(self, value):
        self.value = value
        print(f"Object with value {self.value} created")

    def __del__(self):
        print(f"Object with value {self.value} destroyed")

obj = MyClass(10)
del obj  # Explicitly delete the object
# Output:
# Object with value 10 created
# Object with value 10 destroyed

# Advanced concepts
# 1. Use of context managers: defined using __enter__ and __exit__

class Resource:
    def __enter__(self):
        print("Resource acquired")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Resource released")

with Resource():
    print("Using resource")
# Output:
# Resource acquired
# Using resource
# Resource released

# 2. Use of weak references

import weakref

class MyClass:
    pass

obj = MyClass()
weak_obj = weakref.ref(obj)

print(weak_obj())  # Output: <__main__.MyClass object at 0x...>
del obj
print(weak_obj())  # Output: None
