"""En klasse for å teste resten av programmet"""

from sender import Sender
from receiver import Receiver
from caesar import Caesar
from multiplicative import Multiplicative
from affine import Affine
from unbreakable import Unbreakable
from rsa import RSA
from hacker import Hacker


def test():
    cipher_algorithm = input("Velg en av cipher-algoritmene: ")
    message = input("Skriv inn meldingen som skal krypteres: ")

    if cipher_algorithm == "caesar":
        type = Caesar()

    elif cipher_algorithm == "multiplicative":
        type = Multiplicative()

    elif cipher_algorithm == "affine":
        type = Affine()

    elif cipher_algorithm == "unbreakable":
        type = Unbreakable()

    elif cipher_algorithm == "rsa":
        type = RSA()  # trenger ingen key her

    else:
        print("Illegal cipher algorithm...")

    # skiller mellom RSA og de andre algoritmene, for et eget oppsett
    if cipher_algorithm != "rsa":
        sender = Sender(type, cipher_algorithm)  # oppretter et Sender-objekt
        sender.set_key()  # setter keyen (med mindre er rsa)
        # oppretter et Receiver-objekt
        receiver = Receiver(type, cipher_algorithm)

        crypto = sender.operate_cipher(message)
        print("Dette blir " + crypto + " kryptert")
        result = receiver.operate_cipher(crypto)
        print("Dette blir så dekryptert tilbake til " + result)

    else:
        # setter receiver først, for denne som bestemmer keyen i denne
        # algoritmen
        receiver = Receiver(type, cipher_algorithm)
        receiver.set_key()
        sender = Sender(type, cipher_algorithm)

        crypto = sender.operate_cipher(message)
        print("Når dette krypteres får man da: ")
        print(crypto)
        result = receiver.operate_cipher(crypto)
        print("Dette blir så dekryptert tilbake til " + result)


def test_med_hacker():

    cipher_algorithm = input("Velg en av cipher-algoritmene: ")
    message = input("Skriv inn meldingen som skal krypteres: ")

    if cipher_algorithm == "caesar":
        type = Caesar()

    elif cipher_algorithm == "multiplicative":
        type = Multiplicative()

    elif cipher_algorithm == "affine":
        type = Affine()

    elif cipher_algorithm == "unbreakable":
        type = Unbreakable()

    elif cipher_algorithm == "rsa":
        type = RSA()  # trenger ingen key her

    else:
        print("Illegal cipher algorithm...")

    # skiller mellom RSA og de andre algoritmene, for et eget oppsett
    if cipher_algorithm != "rsa":
        sender = Sender(type, cipher_algorithm)  # oppretter et Sender-objekt
        sender.set_key()  # setter keyen (med mindre er rsa)
        # oppretter et Receiver-objekt
        receiver = Receiver(type, cipher_algorithm)

        crypto = sender.operate_cipher(message)
        print("Dette blir " + crypto + " kryptert")
        result = receiver.operate_cipher(crypto)
        print("Dette blir så dekryptert tilbake til " + result)

        print("\nHacker:")
        hacker = Hacker(type, cipher_algorithm, crypto)

    else:
        # setter receiver først, for denne som bestemmer keyen i denne
        # algoritmen
        receiver = Receiver(type, cipher_algorithm)
        receiver.set_key()
        sender = Sender(type, cipher_algorithm)

        crypto = sender.operate_cipher(message)
        print("Når dette krypteres får man da: ")
        print(crypto)
        result = receiver.operate_cipher(crypto)
        print("Dette blir så dekryptert tilbake til " + result)


test_med_hacker()
