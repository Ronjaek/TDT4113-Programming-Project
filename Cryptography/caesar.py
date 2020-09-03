"""Caesar - krypterer ved å addere på key-verdien"""
from cypher import Cypher


class Caesar(Cypher):
    """Subklasse av Cypher"""

    def __init__(self, key=0):
        super().__init__(key)  # setter først key til 0, for så å endre med metoden set_key

    def encode(self, text):
        """Metode til å kryptere en klar-tekst"""

        self.klar_tekst_start = text

        self.crypto = ""

        # OBS! Python har innebygd ASCII! ord('a') = 97 / chr(97) = 'a'

        for letter in text:
            position = self.find_key(letter)
            # tar modelo så ikke verdien overskrider alfabetet
            # trekker først fra startverdi og så legger til for å få riktig
            # modelo verdi
            temp = (position + self.key -
                    self.first_key) % self.alphabet_lenght + self.first_key
            # finner tilsvarende tegn til den nye posisjonen
            self.crypto += self.alphabet_dict[temp]

        return self.crypto

    def decode(self, crypto):
        """Metode til å dekode eller tyde en kryptering"""

        self.klar_tekst_slutt = ""

        for letter in crypto:
            position = self.find_key(letter)
            temp = (position - self.key -
                    self.first_key) % self.alphabet_lenght + self.first_key
            self.klar_tekst_slutt += self.alphabet_dict[temp]

        return self.klar_tekst_slutt

    def generate_keys(self):
        """I Caesar settes keyen fra start av sender"""

        self.key = int(input("Skriv inn et heltall som skal være key: "))

        return self.key


"""
goCaesar = Caesar(6)

print(goCaesar.encode("eleven"))

print(goCaesar.decode("krk|kt"))
"""
