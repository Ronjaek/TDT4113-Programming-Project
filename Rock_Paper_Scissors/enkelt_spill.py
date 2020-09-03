"""Denne tar for seg en runde med konkurranse mellom de to spillerne"""


class EnkeltSpill:
    """Brukes til å gjennomføre og representere et enkelt spill. Spør etter spillerens valg"""

    def __init__(self, spiller1, spiller2):
        """Initiere en instans av klassen, der spiller1 og spiller2 er de to spillerne"""

        self.spiller1 = spiller1
        self.spiller2 = spiller2

        self.spiller1_trekk = ""
        self.spiller2_trekk = ""

        self.runde_vinner = ""

        self.spiller1_poeng = 0
        self.spiller2_poeng = 0

    def gjennomforer_spill(self, spiller1, spiller2):
        """Spør hver spiller om valget, og bestemmer resultatet"""

        self.spiller1_trekk = spiller1.velg_aksjon()
        self.spiller2_trekk = spiller2.velg_aksjon()

        aksj = Aksjon(self.spiller1_trekk, self.spiller2_trekk)

        if aksj.__gt__(self.spiller1, self.spiller2) == 1:
            self.spiller1_poeng = 1
            self.runde_vinner = self.spiller1

        elif aksj.__gt__(self.spiller1, self.spiller2) == -1:
            self.spiller2_poeng = 1
            self.runde_vinner = self.spiller2

        elif aksj.__gt__(self.spiller1, self.spiller2) == 0:
            self.spiller1_poeng = 0.5
            self.spiller2_poeng = 0.5
            self.runde_vinner = ""

    def get_trekk1(self):
        """returnerer spiller1 sitt trekk"""
        return self.spiller1_trekk

    def get_trekk2(self):
        """returnerer spiller2 sitt trekk"""
        return self.spiller2_trekk

    def get_vinner(self):
        """returnerer denne rundens vinner"""
        return self.runde_vinner

    def get_spiller1_poeng(self):
        """returnerer poengene spiller1 fikk denne runden"""
        return self.spiller1_poeng

    def get_spiller2_poeng(self):
        """returnerer poengene spiller2 fikk denne runden"""
        return self.spiller2_poeng

    def __str__(self):
        """Tekstlig rapportering av enkelt-spill"""

        navn1 = self.spiller1.get_spiller_navn()
        navn2 = self.spiller2.get_spiller_navn()

        resultat = "" + navn1 + " valgte å spille " + self.get_trekk1() + \
                   ", mens " + navn2 + " valgte å spille " + self.get_trekk2() + "\n"

        if self.get_vinner() == self.spiller1:
            resultat += navn1 + " vant derfor denne runden."

        elif self.get_vinner() == self.spiller2:
            resultat += navn2 + " vant derfor denne runden."

        else:
            resultat += "Det ble derfor uavgjort."

        print(resultat)


class Aksjon:
    """Representerer aksjonen som velges - definere om en aksjon vinner over en annen"""

    def __init__(self, aksj1, aksj2):
        """initialiserer verdiene"""
        self.aksj1 = aksj1
        self.aksj2 = aksj2

    def __eq__(self, aksj1, aksj2):
        """sjekker om de er like - true hvis de er"""
        return self.aksj1 == self.aksj2

    def __gt__(self, aksj1, aksj2):
        """sammenlikner to aksjoner"""
        valg_a = Sammenlikning(self.aksj1)
        valg_b = Sammenlikning(self.aksj2)

        if valg_a.vinner_mot == valg_b.valg:
            """returnerer 1 dersom aksj1 vinner over aksj2"""
            return 1

        elif valg_a.taper_mot == valg_b.valg:
            """returnerer -1 dersom aksj2 vinner over aksj1"""
            return -1

        else:
            """indikerer at de er like"""
            return 0


class Sammenlikning:
    """En hjelpeklasse som kun sammenlikner ulike valg"""

    def __init__(self, valg=""):  # instansierer de forskjellige valgene, og tilhørende resultat
        self.valg = valg

        if self.valg == "stein":  # viser utfallene dersom en velger stein
            self.taper_mot = "papir"
            self.vinner_mot = "saks"

        elif self.valg == "saks":
            self.taper_mot = "stein"
            self.vinner_mot = "papir"

        elif self.valg == "papir":
            self.taper_mot = "saks"
            self.vinner_mot = "stein"

        else:
            print("Ugyldig valg. Velg mellom stein, saks eller papir!")

    def print_sammenlikning(self):
        """printer resultatet"""
        print(self.valg)
