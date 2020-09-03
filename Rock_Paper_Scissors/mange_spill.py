"""En klasse for å teste spillerne"""

from enkelt_spill import EnkeltSpill
import matplotlib.pyplot as plt


class MangeSpill:
    """En klasse som starter et enkeltspill, og kjører antall runder som er gitt"""

    def __init__(self, spiller1, spiller2, antall_spill):
        """Registrer til grafen, og setter poeng og antall vinn lik 0 fra start"""

        self.spiller1 = spiller1
        self.spiller2 = spiller2
        """husker antallet ganger de skal spille"""
        self.antall_spill = antall_spill

        self.spiller1_poeng = 0
        self.spiller2_poeng = 0
        self.spiller1_victories = 0
        self.spiller2_victories = 0

        # oppsett til matplotlib
        self.antall_runder = 0
        self.runde_akse = []  # x-aksen
        self.prosent_akse1 = []  # y-aksen
        self.prosent_akse2 = []  # y-akse2

    def arranger_enkeltspill(self):
        """Vurderer valg, sjekk vinner, rapporter valgene og gir tekstlig resultat"""

        nytt_spill = EnkeltSpill(self.spiller1, self.spiller2)

        nytt_spill.gjennomforer_spill(self.spiller1, self.spiller2)

        self.spiller1_poeng += nytt_spill.get_spiller1_poeng()
        self.spiller2_poeng += nytt_spill.get_spiller2_poeng()

        spiller1_trekk = nytt_spill.get_trekk1()
        spiller2_trekk = nytt_spill.get_trekk2()

        if nytt_spill.get_vinner() == self.spiller1:
            self.spiller1_victories += 1
        elif nytt_spill.get_vinner() == self.spiller2:
            self.spiller2_victories += 1

        self.spiller1.oppdater(spiller2_trekk)
        self.spiller2.oppdater(spiller1_trekk)

        nytt_spill.__str__()

    def arranger_turnering(self):
        """Gjennomfører antall_spill og rapporterer gevinst-prosenten når ferdig"""

        for i in range(self.antall_spill):

            self.arranger_enkeltspill()
            self.antall_runder = i + 1
            print(self.antall_runder)
            self.runde_akse.append(self.antall_runder)
            self.prosent_akse1.append(
                self.spiller1_poeng /
                self.antall_runder)
            self.prosent_akse2.append(self.spiller2_poeng / self.antall_runder)

        print("\n" +
              self.spiller1.get_spiller_navn() +
              " vant " +
              str(self.spiller1_victories) +
              " og fikk " +
              str(self.spiller1_poeng) +
              "\n" +
              self.spiller2.get_spiller_navn() +
              " vant " +
              str(self.spiller2_victories) +
              " og fikk " +
              str(self.spiller2_poeng))

        # farger for å skille mellom aksen til spiller1 og 2
        plt.plot(self.runde_akse, self.prosent_akse1, color="red")
        plt.plot(self.runde_akse, self.prosent_akse2, color="blue")
        plt.title(
            "Statistikk over vinn-raten til " +
            self.spiller1.get_spiller_navn() +
            " er rød, og vinn-raten til " +
            self.spiller2.get_spiller_navn() +
            " er blå")
        plt.xlabel("x - Runde")
        plt.ylabel("y - %")
        plt.show()
