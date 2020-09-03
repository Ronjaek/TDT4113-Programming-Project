"""Unbreakable cipher"""
from cypher import Cypher


class Unbreakable(Cypher):
    """Bruker nøkkelord, fremfor tall til kryptering for å gjøre det vanskeligere å hacke"""

    def __init__(self, key=""):
        # setter først key til å være tom "", for så å endre med metoden
        # set_key
        super().__init__(key)

    def encode(self, text):
        """Bruker et nøkkelold for å kryptere for å være vanskeligere å hacke"""

        self.klar_tekst_start = text

        self.crypto = ""

        for i in range(len(text)):
            text_index = self.find_key(text[i])
            # repeterer nøkkelordet så mange gnager at det kommer på lengde med
            # klar-teksten
            key_index = self.find_key(self.key[i % (len(self.key))])
            # legger til tallverdiene i både klar-teksten og nøkkelordet, og
            # regner modelo 95 av dette
            temp = (text_index + key_index -
                    self.first_key) % self.alphabet_lenght + self.first_key
            # finner tilsvarende tegn til den nye posisjonen
            self.crypto += self.alphabet_dict[temp]

        return self.crypto

    def decode(self, crypto):
        """Genererer et nytt nøkkelord, og kaller på encode med dette nøkkelordet"""

        # finner riktig kodeord ved å bytte symbolet som står der med et annet
        original_key = self.key
        decode_keyword = ""

        for i in range(len(original_key)):
            # finner tall-verdien til første bokstav i keyen
            key_index = self.find_key(original_key[i])
            # trekker fra index til første boktav i alfabetet, for så å legge
            # til etter modelo for å få riktig verdi
            decode_number = (self.alphabet_lenght - key_index -
                             self.first_key) % self.alphabet_lenght + self.first_key
            decode_keyword += self.alphabet_dict[decode_number]

        # den nye nøkkelordet kan ses på som den inverse av den originale
        # nøkkelen
        self.key = decode_keyword

        # tar i bruk det nye nøkkelordet, og kaller encode-metoden med
        # krypterings-teksten
        self.klar_tekst_slutt = self.encode(crypto)

        return self.klar_tekst_slutt

    def generate_keys(self):
        """I Unbreakable settes keyen fra start av sender, keyen er her et ord"""

        self.key = input("Skriv inn ordet som skal brukes som key: ")

        return self.key


"""
go = Unbreakable("a")

encrypted = go.encode("asap")
print(encrypted)

print(go.decode(encrypted))
"""
