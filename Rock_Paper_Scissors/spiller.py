"""Fil som oppretter spiller, og de forskjellige spilltypene"""
import random
from enkelt_spill import EnkeltSpill
from enkelt_spill import Sammenlikning


class Spiller:
    """En klasse for alle spillerne"""

    def __init__(self, navn="", spill_type=""):

        self.navn = navn
        self.spill_type = spill_type

        if spill_type == "tilfeldig":
            self.type = Tilfeldig()

        elif spill_type == "sekvensiell":
            self.type = Sekvensiell()

        elif spill_type == "mestVanlig":
            self.type = MestVanlig()

        elif spill_type == "historiker":
            husk = int(input("Hvor mange trekk vil du skal huskes? "))
            self.type = Historiker(husk)
        else:
            print("Denne spilltypen finnes ikke...")

    def velg_aksjon(self):
        """Skal velge hvilken aksjon som skal utføres (spille stein, saks, eller papir)"""

        aksj = self.type.valg()
        return aksj

    def oppdater(self, motstander_trekk):
        """kaller på oppdater-metoden i spillType klassen som er gitt for denne spilleren"""
        self.type.oppdater(motstander_trekk)

    def motta_resultat(self):
        """Mottar resultatet etter hvert enkelt spill - hva begge valgte, og hvem som vant"""

        return EnkeltSpill.__str__()

    def get_spiller_navn(self):
        """returnerer spillerens navn"""

        return self.navn

    def oppgi_trekk_navn(self):
        """oppgir navnet på klassen, så kan rapporteres i grensesnittet"""

        return self.spill_type


class Tilfeldig:
    """Velger tilfeldig mellom stein, saks og papir"""

    def __init__(self):

        self.mulige_trekk = ["stein", "saks", "papir"]

    def valg(self):
        """Trekket som spilleren velger denne runden"""
        num = random.randint(0, 2)
        return self.mulige_trekk[num]

    def oppdater(self, input):
        """Har egt ingen funksjon"""
        return


class Sekvensiell:
    """Går sekvensielt gjennom de forskjellige aksjonene"""

    def __init__(self):

        self.ssp_list = ["stein", "saks", "papir"]
        self.count = 0

    def valg(self):
        """returnerer sekvensielt neste posisjon i SSP_listen"""
        return self.ssp_list[self.count]

    def oppdater(self, input):
        """når oppdater kalles, så får count en ny verdi"""

        if self.count == 2:
            self.count = 0
        else:
            self.count += 1


class MestVanlig:
    """Finner motstanderens mest vanligste trekk"""

    def __init__(self):
        """Obs! Listen definerer det som oftest VINNER over det motstanderen velger"""
        self.ssp_dict = {"stein": 0, "saks": 0, "papir": 0}
        self.ssp_list = ["stein", "saks", "papir"]

    def valg(self):
        """Finner riktig valg"""

        mest_gjentatt = ""
        antall_gjentakelser = 0

        for key, value in self.ssp_dict.items():
            print(key + "->" + str(value))

        for trekk in self.ssp_dict.keys():

            if self.ssp_dict[trekk] >= antall_gjentakelser:
                antall_gjentakelser = self.ssp_dict[trekk]
                mest_gjentatt = trekk
                print(antall_gjentakelser)
                print(mest_gjentatt)

        """tilsvarer at motstanderen ikke har utført et trekk enda"""
        if antall_gjentakelser == 0:
            num = random.randint(0, 2)

            """returnerer trekket som er på posisjon num"""
            return self.ssp_list[num]

        """dette er trekket som har vunnet mest over det motstanderen OFTEST velger"""
        return mest_gjentatt

    def oppdater(self, mostander_verdi):
        """oppretter en instans av Sammenliknings klassen"""
        temp = Sammenlikning(mostander_verdi)

        """legger til en på det trekket i SSP_dict som vinner over motstanderens valg"""
        self.ssp_dict[temp.taper_mot] += 1


class Historiker:
    """starter med å sette husk lik 1"""

    def __init__(self, husk):

        self.motstander_trekk = []
        self.ssp_list = ["stein", "saks", "papir"]
        """lager en tom dictionary, som defineres senere"""
        self.trekk_mot = {}
        """lager en tom liste"""
        self.sekvens = []
        self.kopi_trekk = []

        """husk=1 -> motstanderen spiller oftest etter siste trekk"""
        """husk=2 -> to siste trekk, er komboen brukt før, hva kom etter"""
        if husk >= 0:
            self.husk = husk
        else:
            print("Husk kan ikke være et negativt tall")

    def valg(self):
        """Finner riktig valg for en med denne spilltypen"""

        lengde_mtrekk = len(self.motstander_trekk)

        if (lengde_mtrekk == 0) or (self.husk ==
                                    0):
            return self._random_trekk()

        elif lengde_mtrekk <= self.husk:

            """sekvens skal inneholde like mange elementer som husk"""
            if len(self.sekvens) < self.husk:
                self.sekvens.append(self.motstander_trekk[-1])

            return self._random_trekk()

        else:
            self.sekvens = self.motstander_trekk[-self.husk:]

            print(self.motstander_trekk)
            print(self.sekvens)

            self.kopi_trekk = self.motstander_trekk.copy()

            """trekkene uten siste sekvens"""
            self.kopi_trekk = self.kopi_trekk[:len(
                self.kopi_trekk) - self.husk]
            print(self.kopi_trekk)

            """rangerer trekkene som oftest SLÅR det motstanderen spiller etter sekvensen"""
            self.trekk_mot = {"stein": 0, "saks": 0, "papir": 0}

            """sjekker så lenge starten på sekvensen er med i motstanderens trekk fjerner"""
            while (self.sekvens[0] in self.kopi_trekk) and (
                    len(self.kopi_trekk) > self.husk):

                index_start = self.kopi_trekk.index(self.sekvens[0])

                if self.sekvens == self.kopi_trekk[index_start: (
                        index_start + len(self.sekvens))]:
                    print("den er med!")
                    print(index_start)
                    index_slutt = index_start + len(self.sekvens)

                    """hvis index_slutt er utenfor kopi_trekk, så skal while løkken stoppes"""
                    if index_slutt >= len(self.kopi_trekk):
                        break

                    print(index_slutt)
                    """ser på neste trekk etter sekvensen"""
                    forventet_trekk = self.kopi_trekk[index_slutt]
                    """setter slutten som den nye starten"""
                    self.kopi_trekk = self.kopi_trekk[index_slutt:]
                    print(self.kopi_trekk)

                    temp = Sammenlikning(forventet_trekk)
                    print("1" + forventet_trekk)
                    vinner_trekk = temp.taper_mot
                    print("2" + vinner_trekk)

                    self.trekk_mot[vinner_trekk] += 1

                    for key, value in self.trekk_mot.items():
                        print(key, "->", value)

                else:
                    print("ikke i trekkene")
                    if index_start < len(self.kopi_trekk):
                        self.kopi_trekk = self.kopi_trekk[index_start + 1:]
                    else:
                        break

        """dersom sekvensen aldri har vært utført tidligere"""
        if all(value == 0 for value in self.trekk_mot.values()):
            return self._random_trekk()

        else:

            antall = 0
            flest = ""

            for trekk in self.trekk_mot:

                if self.trekk_mot[trekk] >= antall:
                    antall = self.trekk_mot[trekk]
                    flest = trekk

            return flest

    def _random_trekk(self):
        """En metode for å finne et tilfeldig trekk"""

        num = random.randint(0, 2)
        return self.ssp_list[num]

    def oppdater(self, forrige_trekk_motstander):
        """Når husk er større enn 1 leter Historiker etter"""

        self.motstander_trekk.append(forrige_trekk_motstander)
