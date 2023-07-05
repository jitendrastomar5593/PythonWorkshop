class MyClass:
    def __init__(self):
        self.public_attribute = 'Public'            # Public attribute
        self._protected_attribute = 'Protected'     # Protected attribute
        self.__private_attribute = 'Private'        # Private attribute

    def public_method(self):
        print('This is a public method.')

    def _protected_method(self):
        print('This is a protected method.')

    def __private_method(self):
        print('This is a private method.')

    def access_members(self):
        print('Accessing members:')
        print('Public attribute:', self.public_attribute)
        print('Protected attribute:', self._protected_attribute)
        print('Private attribute:', self.__private_attribute)
        self.public_method()
        self._protected_method()
        self.__private_method()

# Creating an instance of the class
obj = MyClass()

# Accessing members
print('Accessing members from outside the class:')
print('Public attribute:', obj.public_attribute)
print('Protected attribute:', obj._protected_attribute)

# Accessing methods
obj.public_method()
obj._protected_method()
obj.access_members()
