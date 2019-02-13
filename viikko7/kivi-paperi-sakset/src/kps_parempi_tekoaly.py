from tuomari import Tuomari
from tekoaly_parannettu import TekoalyParannettu
from peli import Peli

class KPSParempiTekoaly(Peli):
    def __init__(self):
        self.tekoaly = TekoalyParannettu(10)
    
    def get_toka_siirto(self, ekan_siirto):
        tokan_siirto = self.tekoaly.anna_siirto()

        print(f"Tietokone valitsi: {tokan_siirto}")
        self.tekoaly.aseta_siirto(ekan_siirto)
        return tokan_siirto
