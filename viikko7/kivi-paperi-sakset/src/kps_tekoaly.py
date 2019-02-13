from tuomari import Tuomari
from tekoaly import Tekoaly
from peli import Peli


class KPSTekoaly(Peli):
    def __init__(self):
        self.tekoaly = Tekoaly()
    
    def get_toka_siirto(self, ekan_siirto):
        tokan_siirto = self.tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {tokan_siirto}")
        return tokan_siirto

