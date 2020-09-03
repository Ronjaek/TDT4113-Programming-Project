from cypher import Cypher
from multiplicative import Multiplicative
from caesar import Caesar


class Affine(Cypher):
    """Kan ses på som en blanding av Multiplicative og Caesar"""

    def __init__(self, key=(0, 0)):
        super().__init__(key)  # setter først key til (0,0), for så å endre med metoden set_key

    def encode(self, text):

        self.klar_tekst_start = text

        """Krypterer teksten ved å ta inn to keys i form av en tuple"""
        temp1 = Multiplicative(
            self.key[0])  # oppretter et midlertidig objekt med angitt key
        temp2 = Caesar(self.key[1])

        temp_text = temp1.encode(text)
        self.crypto = temp2.encode(temp_text)

        return self.crypto

    def decode(self, crypto):
        """Dekrypterer her ved bruk av to nøkler"""

        temp1 = Multiplicative(self.key[0])
        temp2 = Caesar(self.key[1])

        temp_crypto = temp2.decode(crypto)
        self.klar_tekst_slutt = temp1.decode(temp_crypto)

        return self.klar_tekst_slutt

    def generate_keys(self):
        """I Affine settes tuppelen av keyer fra start av sender"""

        key1 = int(input(
            "Skriv inn den første keyen som skal brukes til multiplikasjons-cipheret: "))
        key2 = int(
            input("Skriv inn den andre keyen som skal brukes til Caesar-cipheret: "))

        self.key = (key1, key2)

        return self.key


go = Affine((2, 4))

print(go.encode("hello"))
print(go.decode("uo}}$"))
