from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote
        self.kori = []

    def tavaroita_korissa(self):
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 
        tavaroita = 0
        for ostos in self.kori:
            tavaroita += ostos.lukumaara()
        return tavaroita

    def hinta(self):
        # kertoo korissa olevien ostosten yhteenlasketun hinnan
        hinta = 0
        for ostos in self.kori:
            hinta += ostos.hinta()
        return hinta

    def lisaa_tuote(self, lisattava: Tuote):
        # lisää tuotteen
        ostos_korissa = next((ostos for ostos in self.kori if ostos.tuotteen_nimi() == lisattava.nimi()), None)
        if ostos_korissa is None:
            self.kori.append(Ostos(lisattava))
        else:
            ostos_korissa.muuta_lukumaaraa(1)

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        ostos_korissa = next((ostos for ostos in self.kori if ostos.tuotteen_nimi() == poistettava.nimi()), None)
        ostos_korissa.muuta_lukumaaraa(-1)
        if ostos_korissa.lukumaara() == 0:
            self.kori.remove(ostos_korissa)

    def tyhjenna(self):
        # tyhjentää ostoskorin
        self.kori = []

    def ostokset(self):
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
        return self.kori

