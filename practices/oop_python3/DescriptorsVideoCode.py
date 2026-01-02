class ReadOnlyError(Exception):
    """Raised when a value is attempted to bet set."""


class ReadOnlyValue:
    def __init__(self, value):
        self.value = value

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        raise ReadOnlyError(f"'my_value' cannot be set, you provided: {value}")

class SomeClass:
    my_value = ReadOnlyValue(1234)

x = SomeClass()
print(x.my_value)
x.my_value = "hello!"