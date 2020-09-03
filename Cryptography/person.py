"""Oppretter personene som brukes til å motta, sende og evt hacke det som sendes"""


class Person:
    """to/tre personer: en som sender melding, en som mottar og evt. en som forsøker hacke"""

    def __init__(self, type_algorithm, cipher_algorithm):
        """en instans av en av subklassene til Cypher"""

        self.type_algorithm = type_algorithm
        self.cipher_algorithm = cipher_algorithm
        self.key = None  # settes til none fra start, men endres fra sender-klassen

    def set_key(self):
        """Metoden blir overskevet i sender klassen - kun en dummy-metode"""

    def get_key(self):
        """Returnerer en persons key"""

        return self.key

    def operate_cipher(self):
        """Metoden blir overskrevet i sender/reciever - kun en dummy-metode"""
