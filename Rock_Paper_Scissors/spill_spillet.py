"""Bruker denne filen til å kjøre alt"""
from mange_spill import MangeSpill
from spiller import Spiller


def spill():
    """Setter navn, spilltype og oppretter spillere"""

    spiller1_navn = input("Skriv inn navnet til spiller nr.1: ")
    spiller2_navn = input("Skriv inn navnet til spiller nr.2: ")

    """endrer fra string til int"""
    antall_spill = int(input("Skriv inn antall runder som skal spilles: "))

    if spiller1_navn == "":
        spiller1_navn = "spiller1"
    if spiller2_navn == "":
        spiller2_navn = "spiller2"

    gyldig_spille_type = [
        "tilfeldig",
        "sekvensiell",
        "mestVanlig",
        "historiker"]

    spill_type1 = input("Velg spillestil for " + spiller1_navn + ": ")
    while spill_type1 not in gyldig_spille_type:
        # for å sjekke at spillTypen som skrives inn er gyldig
        print("Spilletypen du skrev inn er ikke gyldig")
        spill_type1 = input("Velg spillestil for " + spiller1_navn + ": ")

    spille_type2 = input("Velg spillestil for " + spiller2_navn + ": ")
    while spille_type2 not in gyldig_spille_type:
        # for å sjekke at spillTypen som skrives inn er gyldig
        print("Spilletypen du skrev inn er ikke gyldig")
        spille_type2 = input("Velg spillestil for " + spiller2_navn + ": ")

    # oppretter en instans av Spiller med spillTypen
    spiller1 = Spiller(spiller1_navn, spill_type1)
    spiller2 = Spiller(spiller2_navn, spille_type2)

    # oppretter en instans av MangeSpill
    nytt_game = MangeSpill(spiller1, spiller2, antall_spill)
    # nyttGame.arranger_enkeltspill()
    nytt_game.arranger_turnering()


spill()
