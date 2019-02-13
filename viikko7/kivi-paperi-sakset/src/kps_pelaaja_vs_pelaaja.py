from tuomari import Tuomari
from peli import Peli


class KPSPelaajaVsPelaaja(Peli):
    def get_toka_siirto(self, ekan_siirto):
        tokan_siirto = input("Toisen pelaajan siirto: ")
        return tokan_siirto

