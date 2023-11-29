OLETUSKAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko
    
    def __init__(self, kapasiteetti=OLETUSKAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko

        self.ljono = self._luo_lista(self.kapasiteetti)

        self.alkioiden_lkm = 0

    def kuuluu(self, n):
        return n in self.ljono

    def lisaa(self, n):
        if not self.kuuluu(n):
            self.ljono[self.alkioiden_lkm] = n
            self.alkioiden_lkm = self.alkioiden_lkm + 1

            # ei mahdu enempää, luodaan uusi säilytyspaikka luvuille
            if self.alkioiden_lkm == len(self.ljono):
                self.kasvata_puskuria()
            return True

        return False
    
    def kasvata_puskuria(self):
        uusi_lista = self._luo_lista(self.alkioiden_lkm + self.kasvatuskoko)
        self.kopioi_lista(self.ljono, uusi_lista)
        self.ljono = uusi_lista

    def poista(self, n):
        if self.kuuluu(n):
            kohta = self.ljono.index(n)
            for j in range(kohta, self.alkioiden_lkm - 1):
                self.ljono[j] = self.ljono[j + 1]
            self.ljono[self.alkioiden_lkm - 1] = 0
            self.alkioiden_lkm = self.alkioiden_lkm - 1
            return True
        return False

    def kopioi_lista(self, kopioitava_lista, kopioitu_lista):
        for i in range(0, len(kopioitava_lista)):
            kopioitu_lista[i] = kopioitava_lista[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = self._luo_lista(self.alkioiden_lkm)
        for i in range(0, len(taulu)):
            taulu[i] = self.ljono[i]

        return taulu

    @staticmethod
    def yhdiste(a, b):
        result = IntJoukko()
        apu_lista = a.to_int_list()
        apu_lista.extend(b.to_int_list())
        for x in apu_lista:
            result.lisaa(x)
        return result

    @staticmethod
    def leikkaus(a, b):
        result = IntJoukko()
        for x in a.to_int_list():
            if b.kuuluu(x):
                result.lisaa(x)
        return result

    @staticmethod
    def erotus(a, b):
        result = IntJoukko()
        for x in a.to_int_list():
            result.lisaa(x)
        for x in b.to_int_list():
            result.poista(x)
        return result

    def __str__(self):
        result = ''
        for i,x in enumerate(self.to_int_list()):
            result += str(x)
            if i != self.alkioiden_lkm-1:
                result += ', '
        return '{' + result + '}'

      