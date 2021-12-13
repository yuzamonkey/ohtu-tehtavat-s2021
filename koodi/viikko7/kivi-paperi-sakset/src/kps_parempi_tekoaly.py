from kps import KPS
from tekoaly_parannettu import TekoalyParannettu


class KPSParempiTekoaly(KPS):
    def __init__(self):
        super().__init__()
        self.tekoaly = TekoalyParannettu(10)

    def _toisen_siirto(self, ensimmaisen_siirto):
        if self._onko_ok_siirto(ensimmaisen_siirto):
            siirto = self.tekoaly.anna_siirto()
            print(f"Tietokone valitsi: {siirto}")
            return siirto
        return None
