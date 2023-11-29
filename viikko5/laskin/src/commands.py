

class Summa:
    def __init__(self, sovellus, lue_arvo):
        self.sovellus = sovellus
        self.lue_arvo = lue_arvo

    def suorita(self):
        self.sovellus.plus(self.lue_arvo())

class Erotus:
    def __init__(self, sovellus, lue_arvo):
        self.sovellus = sovellus
        self.lue_arvo = lue_arvo

    def suorita(self):
        self.sovellus.miinus(self.lue_arvo())

class Nollaus:
    def __init__(self, sovellus, lue_arvo):
        self.sovellus = sovellus
        self.lue_arvo = lue_arvo

    def suorita(self):
        self.sovellus.nollaa()

class Kumoa:
    def __init__(self, sovellus, lue_arvo):
        self.sovellus = sovellus
        self.lue_arvo = lue_arvo

    def suorita(self):
        self.sovellus.peruuta()
        