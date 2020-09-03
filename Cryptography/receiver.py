"""Subklasse av Person"""
from person import Person


class Receiver(Person):  # arver fra klassen Person
    """Setter keyen om RSA, ellers prøver kun å dekryptere melding fra sender"""

    def __init__(self, type_algorithm, cipher_algorithm):
        super().__init__(type_algorithm, cipher_algorithm)
        self.secret_key = None
        self.crypto = ""

    def set_key(self):
        """Setter keyen som brukes til valgt krypteringsalgoritme"""

        # RSA er den eneste krypteringsalgoritmen hvor keyen settes fra
        # mottaker
        if self.cipher_algorithm == "rsa":
            # kaller på metoden som returnerer to variabler
            key, secret_key = self.type_algorithm.generate_keys()

            self.key = key  # setter den offentlige nøkkelen
            self.secret_key = secret_key  # setter den hemmelige nøkkelen, gjøres kun ved RSA

        else:
            pass

    def operate_cipher(self, crypto):
        """Konverterer en kryptert melding itl klar-tekst"""

        self.crypto = crypto  # lagrer den krypterte meldingen

        # kaller på type cipher-algotihm for å kunne oversette riktig
        text = self.type_algorithm.decode(crypto)

        return text
