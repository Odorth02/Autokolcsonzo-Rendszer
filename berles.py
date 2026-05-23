from jarmuvek import Auto
from datetime import datetime

class Berles:
    def __init__(self, auto:Auto, datum_str :str, berlo_neve: str):
        self._auto = auto
        self._berlo_neve = berlo_neve

        try:
            valid_datum = datetime.strptime(datum_str, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError(f"Hibás dátum! (ÉÉÉÉ-HH-NN)")
        if valid_datum < datetime.now().date():
            raise ValueError("Nem lehet múltbeli dátumra autót bérelni!")
        self._datum = valid_datum

    @property
    def berlo_neve(self):
        return self._berlo_neve
    @property
    def auto(self):
        return self._auto
    @property
    def datum(self):
        return self._datum.strftime("%Y/%m/%d")
    @property
    def info(self):
        return f"Jármű: {self._auto.tipus}, {self._auto.rendszam} | Dátum: {self._datum} | Bérlő:{self._berlo_neve} | Ár: {self._auto.berleti_dij} Ft/nap"
