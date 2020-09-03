"""Subklasse av Container"""
from container import Container

class Stack(Container):

    def __init__(self):
        """instansiering gjort i superklassen"""
        super(Stack, self).__init__()

    def peek(self):
        """returnerer siste elementet i listen, ikke fjern det"""

        assert not self.is_empty()
        return self._items[-1]

    def pop(self):
        """fjerner her det siste elementet"""

        assert not self.is_empty()
        return self._items.pop(-1)

    def unit_test(self):

        for i in range(10):
            super().push(i)

        while not super().is_empty():
            print(self.pop())


"""
stack = Stack()
print(stack.unit_test())
"""
