"""En subklasse av Person"""
from person import Person


class Sender(Person):
    """Setter en key, og krypterer en melding ut ifra denne keyen"""

    def __init__(self, type_algorithm, cipher_algorithm):
        """Type cipher_algorithm settes fra Sender"""
        super().__init__(type_algorithm, cipher_algorithm)

    def set_key(self):
        """Setter keyen som brukes til valgt krypteringsalgoritme"""

        # med mindre valgt krypteringsalgoritme er rsa, så settes keyen fra
        # sender-klassen
        if self.cipher_algorithm != "rsa":
            # kaller på metoden i hver av algoritme
            self.key = self.type_algorithm.generate_keys()
        else:
            pass

    # senderen generer cipher-tekst
    def operate_cipher(self, text):
        """Senderen skal generere en cipher tekst av klar-tekst"""

        # kaller på type cipher-algorithm og ecode-metoden
        crypto = self.type_algorithm.encode(text)

        return crypto
