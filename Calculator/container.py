"""Superklassen Container"""

class Container():

    def __init__(self):
        """konstruktøren oppretter en tom liste"""
        self._items = []  # oppretter en privat liste

    def size(self):
        """returnerer antall elementer i liste"""

        return len(self._items)

    def is_empty(self):
        """sjekker om self._items er tom"""

        if len(self._items) == 0:
            return True

        return False

    def push(self, item):
        """legger til et element på slutten av listen"""

        self._items.append(item)

    def pop(self):
        """Fjerner riktig element avhengig av Queue eller Stack, og returner det"""

        raise NotImplementedError  # feilmelding dersom ikke implementeres

    def peek(self):
        """returner topp elmentet uten å fjerne det - overskrives i subklassene"""

        raise NotImplementedError
