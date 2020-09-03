"""En subklasse av Container"""
from container import Container


class Queue(Container):

    def __init__(self):
        """instansiering gjort i superklassen"""
        super(Queue, self).__init__()

    def peek(self):
        """returnerer første elementet i listen, ikke fjern det"""

        assert not self.is_empty()
        return self._items[0]

    def pop(self):
        """fjerner det første elementet"""

        assert not self.is_empty()
        return self._items.pop(0)

    def unit_test(self):

        for i in range(10):
            super().push(i)

        while not super().is_empty():
            print(self.pop())


"""
queue = Queue()
print(queue.unit_test())
"""

