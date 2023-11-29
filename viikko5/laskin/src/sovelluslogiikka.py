class Sovelluslogiikka:
    def __init__(self, arvo=0):
        self._arvo = arvo
        self._muisti = [arvo]
    
    def update_muisti(self):
        self._muisti.append(self._arvo)
    
    def peruuta(self):
        if len(self._muisti) > 1:
            self._muisti.pop()
            self._arvo = self._muisti[-1]

    def miinus(self, operandi):
        self._arvo = self._arvo - operandi
        self.update_muisti()

    def plus(self, operandi):
        self._arvo = self._arvo + operandi
        self.update_muisti()

    def nollaa(self):
        self._arvo = 0
        self.update_muisti()

    def aseta_arvo(self, arvo):
        self._arvo = arvo
        
    def arvo(self):
        return self._arvo
