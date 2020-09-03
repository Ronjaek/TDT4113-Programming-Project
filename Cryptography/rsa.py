"""RSA"""
import random
from cypher import Cypher
from crypto_utils import generate_random_prime
from crypto_utils import modular_inverse
from crypto_utils import blocks_from_text
from crypto_utils import text_from_blocks


class RSA(Cypher):
    """I motsetning til annen kryptering trenger ikke mottaker og sender sin key å matche"""

    def __init__(self, key=(0, 0)):
        """Brukes kun for at key skal ha en tom verdi fra start"""
        super().__init__(key)  # setter først key til å være tom "", for så å endre til faktiske key med metoden set_key
        self.secret_key = (0, 0)

    def encode(self, text):
        """Metode til å kryptere en klar-tekst"""

        self.klar_tekst_start = text

        # tar inn en tekst, og returnerer en liste med heltall for kryptering
        # tar inn 1 som block_size, for da får jeg en posisjon per bokstav i
        # teksten
        blocks = blocks_from_text(text, 2)

        self.crypto = []

        # splitter keyen som kommer som en tuple til to forskjellige variabler
        sum_primes = self.key[0]
        rand_num = self.key[1]

        for number in blocks:  # iterer gjennom elementene i blokken
            # en innebygd funksjon i python
            temp = pow(number, rand_num, sum_primes)
            self.crypto.append(temp)

        return self.crypto

    def decode(self, blocks):
        """Dekode eller tyde en kryptering, tar i bruk secret_key for å gjøre det"""

        decoded_numbers = []

        # splitter den hemmelige nøkkelen som kommer i form av en tuple i to
        # variabler
        sum_primes = self.secret_key[0]
        inverse_rand_num = self.secret_key[1]

        for number in blocks:

            decoded_number = pow(number, inverse_rand_num, sum_primes)
            decoded_numbers.append(decoded_number)

        # sette sammen dekrypterte heltallene til klar-teksten igjen
        self.klar_tekst_slutt = text_from_blocks(decoded_numbers, 8)

        return self.klar_tekst_slutt

    def generate_keys(self):
        """Genererer to nøkler, en offentlig til sender og en hemmelig til mottaker"""
        # vanskelig å finne dekrypteringsnøkkel til denne
        numb_bits = 8  # trenger ikke mer enn 8 bits for å representere ASCII

        # generer et random primtall med gitt antall bits
        prime1 = generate_random_prime(numb_bits)
        prime2 = generate_random_prime(numb_bits)

        while prime1 == prime2:
            prime1 = generate_random_prime(numb_bits)
            prime2 = generate_random_prime(numb_bits)

        sum_primes = prime1 * prime2
        phi = (prime1 - 1) * (prime2 - 1)

        rand_num = random.randint(3, phi - 1)  # genererer et tilfeldig heltall

        inverse_rand_num = modular_inverse(rand_num, phi)

        while inverse_rand_num is False:
            inverse_rand_num = modular_inverse(rand_num, phi)

        # offentlig nøkkel som sender skal bruke for å kryptere meldinger
        # kan offentliggjøres, for vanskelig å bryte
        self.key = (sum_primes, rand_num)

        # hemmelig nøkkel, kun mottaker skal ha tilgang på denne
        self.secret_key = (sum_primes, inverse_rand_num)

        return self.key, self.secret_key
