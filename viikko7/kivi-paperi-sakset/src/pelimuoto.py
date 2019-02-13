from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly

class Pelimuoto:
    def __init__(self):
        pass

    @staticmethod
    def luo_kaksinpeli():
        return KPSPelaajaVsPelaaja()

    @staticmethod
    def luo_helppo_tekoalypeli():
        return KPSTekoaly()

    @staticmethod
    def luo_vaikea_tekooalypeli():
        return KPSParempiTekoaly()




        