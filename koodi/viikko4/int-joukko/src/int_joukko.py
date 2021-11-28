KAPASITEETTI = 5
KASVATUSKOKO = 5


class IntJoukko:
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=KASVATUSKOKO):
        self.kapasiteetti = max(0, int(kapasiteetti))
        self.kasvatuskoko = max(0, int(kasvatuskoko))

        self.lukujono = [0] * self.kapasiteetti
        self.alkioiden_lkm = 0

    def kuuluu(self, luku):
        for i in range(0, self.alkioiden_lkm):
            if luku == self.lukujono[i]:
                return True
        return False

    def lisaa(self, luku):
        if not self.kuuluu(luku):
            self.lukujono[self.alkioiden_lkm] = luku
            self.alkioiden_lkm = self.alkioiden_lkm + 1
            self.kasvata_taulukkoa()

    def kasvata_taulukkoa(self):
        if self.alkioiden_lkm % len(self.lukujono) == 0:
            vanha_lukujono = self.lukujono
            self.kopioi_taulukko(self.lukujono, vanha_lukujono)
            self.lukujono = [0] * (self.alkioiden_lkm + self.kasvatuskoko)
            self.kopioi_taulukko(vanha_lukujono, self.lukujono)

    def poista(self, luku):
        indeksi = self.luvun_indeksi(luku)
        aputaulukko = 0

        if indeksi != -1:
            self.lukujono[indeksi] = 0
            for j in range(indeksi, self.alkioiden_lkm - 1):
                aputaulukko = self.lukujono[j]
                self.lukujono[j] = self.lukujono[j + 1]
                self.lukujono[j + 1] = aputaulukko

            self.alkioiden_lkm = self.alkioiden_lkm - 1

    def luvun_indeksi(self, luku):
        for i in range(0, self.alkioiden_lkm):
            if luku == self.lukujono[i]:
                return i
        return -1

    def kopioi_taulukko(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def numerot_listana(self):
        taulu = [0] * self.alkioiden_lkm

        for i in range(0, len(taulu)):
            taulu[i] = self.lukujono[i]

        return taulu

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.numerot_listana()
        b_taulu = b.numerot_listana()

        for i in range(0, len(a_taulu)):
            x.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            x.lisaa(b_taulu[i])

        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.numerot_listana()
        b_taulu = b.numerot_listana()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    y.lisaa(b_taulu[j])

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.numerot_listana()
        b_taulu = b.numerot_listana()

        for i in range(0, len(a_taulu)):
            z.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            z.poista(b_taulu[i])

        return z

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        elif self.alkioiden_lkm == 1:
            return "{" + str(self.lukujono[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.alkioiden_lkm - 1):
                tuotos = tuotos + str(self.lukujono[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.lukujono[self.alkioiden_lkm - 1])
            tuotos = tuotos + "}"
            return tuotos
