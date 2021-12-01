class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = tulos
        self.edellinen = None

    def miinus(self, arvo):
        self.edellinen = self.tulos
        self.tulos = self.tulos - arvo

    def plus(self, arvo):
        self.edellinen = self.tulos
        self.tulos = self.tulos + arvo

    def nollaa(self):
        self.tulos = 0
        self.edellinen = None

    def aseta_arvo(self, arvo):
        self.edellinen = self.tulos
        self.tulos = arvo

    def kumoa(self):
        if self.edellinen is not None:
            self.tulos = self.edellinen
            self.edellinen = None
