from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly


class Peli:
    @staticmethod
    def luo_kaksinpeli():
        return KPSPelaajaVsPelaaja()

    @staticmethod
    def luo_peli_tietokonetta_vastaan():
        return KPSTekoaly()

    @staticmethod
    def luo_peli_paranneltua_tietokonetta_vastaan():
        return KPSParempiTekoaly()
