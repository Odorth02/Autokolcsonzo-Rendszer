from abc import ABC, abstractmethod

class Auto(ABC):
    def __init__(self, rendszam, tipus, berleti_dij):
        self._rendszam = str(rendszam).upper()
        self._tipus = tipus

        if berleti_dij <= 0:
            raise ValueError("A bérleti díjnak pozitív számnak kell lennie!")
        self._berleti_dij = berleti_dij

    @property
    def rendszam(self):
        return self._rendszam
    @property
    def tipus(self):
        return self._tipus
    @property
    def berleti_dij(self):
        return self._berleti_dij
    @abstractmethod
    def auto_info(self):
        pass

class Szemelyauto(Auto):
    def __init__(self, rendszam, tipus, berleti_dij, ferohely):
        super().__init__(rendszam, tipus, berleti_dij)
        if ferohely <= 0:
            raise ValueError("A férőhelyek száma pozitív kell legyen!")
        self._ferohely = ferohely

    @property
    def ferohely(self):
        return self._ferohely
    @property
    def auto_info(self):
        return f"Személyautó: {self._rendszam}, {self._tipus}, {self._ferohely} {self._berleti_dij}"

class Teherauto(Auto):
    def __init__(self, rendszam, tipus, berleti_dij, teherbiras):
        super().__init__(rendszam, tipus, berleti_dij)
        if teherbiras <= 0:
            raise ValueError("A teherbírás pozitív kell legyen!")
        self._teherbiras = teherbiras

    @property
    def teherbiras(self):
        return self._teherbiras
    @property
    def auto_info(self):
        return f"Teherautó: {self._rendszam}, {self._tipus}, {self._teherbiras}, {self._berleti_dij} Ff/nap"
