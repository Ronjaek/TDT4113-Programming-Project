"""Hacker, subklasse av Person"""
from receiver import Receiver
from caesar import Caesar
from multiplicative import Multiplicative
from affine import Affine
from unbreakable import Unbreakable


class Hacker(Receiver):
    """Skal kunne hacke alle cipherne bortsett fra RSA ved bruk av brute-force"""

    def __init__(self, type_algorithm, cipher_algorithm, crypto):
        super().__init__(type_algorithm, cipher_algorithm)

        if self.cipher_algorithm == "caesar":
            self.hack_caesar(crypto)

        elif self.cipher_algorithm == "multiplicative":
            self.hack_multiplicative(crypto)

        elif self.cipher_algorithm == "affine":
            self.hack_affine(crypto)

        elif self.cipher_algorithm == "unbreakable":
            self.hack_unbreakable(crypto)

        else:
            print("Algoritmen er ikke mulig å hacke...")

    def hack_caesar(self, crypto):
        """Prøve å hacke caesar-algoritmen"""

        # vet at nøkkelen er en verdi fra 0 til 95 (lengden på alfabetet)
        for i in range(95):

            temp = Caesar(i)  # kaller på klassen Caesar med key gitt i
            hidden_message = temp.decode(crypto)
            # lager en liste hvor hvert ord i meldingen er et elemnt i listen
            message_list = hidden_message.split()
            counter = 0

            """
            for j in message_list:
                print(j)
            """

            try:
                # prøver å åpne ordfilen for lesing
                with open("english_words.txt", "r") as file:
                    for linje in file.readlines():
                        linje = linje.strip()  # fjerner evt mellomrom etter ordet i filen

                        if linje in message_list:
                            counter += 1  # teller antall ord som faktisk er et engelsk ord
                        # hvert ord i meldingen er faktiske ord
                        if counter == len(message_list):
                            print(
                                "Med keyen " +
                                str(i) +
                                " får man: \n" +
                                hidden_message)
                            return hidden_message

            except FileNotFoundError:
                print("Filen finnes ikke...")

        return "Greide ikke å dekryptere meldingen..."

    def hack_multiplicative(self, crypto):
        """Prøver å hacke multiplicative-algoritmen"""

        for i in range(95):
            temp = Multiplicative(i)
            hidden_message = temp.decode(crypto)
            # gjør om meldingen som tas inn til en liste - hvert ord er et
            # element
            message_list = hidden_message.split()
            counter = 0

            """
            for word in message_list:
                print(word)
            """

            try:
                with open("english_words.txt", "r") as file:
                    for linje in file.readlines():
                        linje = linje.strip()

                        if linje in message_list:
                            counter += 1
                        if counter == len(message_list):
                            print("Med keyen " + str(i) + " får man: \n" +
                                  hidden_message)
                            return hidden_message

            except FileNotFoundError:
                print("Filen finnes ikke...")

        return "Greide ikke å dekryptere meldingen..."

    def hack_affine(self, crypto):
        """Prøver å hacke affine-algoritmen"""

        # er her nødt til å bruke en dobbel for-loop fordi det er to keyer jeg
        # leter etter
        for i in range(95):
            for j in range(95):
                temp = Affine((i, j))
                hidden_message = temp.decode(crypto)

                if hidden_message is not False:

                    message_list = hidden_message.split()
                    counter = 0

                    """
                    for k in message_list:
                        print(k)
                    """

                    try:
                        with open("english_words.txt", "r") as file:
                            for linje in file.readlines():
                                linje = linje.strip()

                                if linje in message_list:
                                    counter += 1
                                if counter == len(message_list):
                                    print(
                                        "Med keyene " +
                                        str(i) +
                                        " og " +
                                        str(j) +
                                        " får man: \n" +
                                        hidden_message)
                                    return hidden_message

                    except FileNotFoundError:
                        print("Finner ikke filen...")

        return "Greide ikke å dekryptere meldingen"

    def hack_unbreakable(self, crypto):
        """Prøver å hacke unbreakable-algoritmen"""

        # legger til hvert av ordene i "english_words.txt" inn i en liste, for
        # å kunne iterere gjnnom
        word_list = []

        try:
            with open("english_words.txt", "r") as file:
                for linje in file.readlines():
                    linje = linje.strip()
                    word_list.append(linje)
        except FileNotFoundError:
            print("Finner ikke filen...")

        counter = 0
        for i in word_list:
            temp = Unbreakable(i)
            hidden_message = temp.decode(crypto)
            print(hidden_message)
            # oppretter en liste av hvert ord som produseres av den satte keyen
            message_list = hidden_message.split()

            for j in word_list:
                if j in message_list:
                    counter += 1
                if counter == len(message_list):
                    print(
                        "Med keyen " +
                        str(i) +
                        " får man meldingen: \n" +
                        hidden_message)
                    return hidden_message

        return "Greide ikke å dekryptere meldingen..."


"""
hack = Hacker(Caesar(), "caesar")
hack.hack_caesar("krk|kt")
"""
"""
goHack = Hacker(Affine(), "affine", "uo}}$")
goHack.hack_affine()
"""
"""
go = Hacker(Multiplicative(), "multiplicative")
go.hack_multiplicative("uo}}$")
"""
"""
go = Hacker(Unbreakable(), "unbreakable")
go.hack_unbreakable("cucr")
"""
