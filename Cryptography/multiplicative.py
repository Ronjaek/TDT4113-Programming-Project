"""Subklasse av Cypher"""
from cypher import Cypher
from crypto_utils import modular_inverse


class Multiplicative(Cypher):
    """Her ganger man hver posisjon av en bokstav i alfabetet med nøkkelen"""

    def __init__(self, key=0):
        super().__init__(key)  # setter først key til 0, for så å endre med metoden set_key
        self.new_key = ""

    def encode(self, text):
        """Gjør om fra klar-tekst til kryptering"""

        self.klar_tekst_start = text

        self.crypto = ""

        for letter in text:
            position = self.find_key(letter)
            # tar modelo så ikke verdien overskrider alfabetet
            # trekker først fra startverdi og så legger til for å få riktig
            # modelo verdi
            temp = (position * self.key -
                    self.first_key) % self.alphabet_lenght + self.first_key
            # finner tilsvarende tegn til den nye posisjonen
            self.crypto += self.alphabet_dict[temp]

        return self.crypto

    def decode(self, crypto):
        """Gjør om fra kryptering til klar-teksts"""

        self.klar_tekst_slutt = ""
        # en nøkkel til dekryptering som passer med den originale nøkkelen
        self.new_key = modular_inverse(self.key, self.alphabet_lenght)

        for letter in crypto:
            position = self.find_key(letter)
            temp = (position * self.new_key -
                    self.first_key) % self.alphabet_lenght + self.first_key
            self.klar_tekst_slutt += self.alphabet_dict[temp]

        return self.klar_tekst_slutt

    def generate_keys(self):
        """I Mutiplicative settes den originale keyen fra start av sender"""

        self.key = int(input("Skriv inn et heltall som skal være key: "))

        return self.key


"""
go = Multiplicative(6)

print(go.encode("fear me"))

print(go.decode("*$kraT$"))
"""
