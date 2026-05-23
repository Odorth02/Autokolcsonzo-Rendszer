from jarmuvek import Auto
from berles import Berles

class Autokolcsonzo:
    def __init__(self, nev):
        self._nev = nev
        self._autok = []
        self._berlesek = []

    @property
    def nev(self):
        return self._nev

    def auto_hozzaadas(self, auto: Auto):
        self._autok.append(auto)

    def autok_listazasa(self):
        if not self._autok:
            print("Az autok listája üres")
            return
        print(f"\n--- {self._nev} ---")
        for auto in self._autok:
            print(auto.auto_info)

    def auto_berles(self, rendszam, datum_str, berlo_neve):
        rendszam = rendszam.upper().strip()
        kivalasztott_auto = None
        for auto in self._autok:
            if auto.rendszam == rendszam:
                kivalasztott_auto = auto
                break
        if not kivalasztott_auto:
            print("Nem található ilyen rendszámú autó!")
            return 0
        for berles in self._berlesek:
            if berles.auto.rendszam == rendszam and berles.datum == datum_str:
                print(f"A(z) {rendszam} rendszámú autó foglalt {datum_str} napon")
                return 0
        try:
            uj_berles = Berles(kivalasztott_auto, datum_str, berlo_neve)
            self._berlesek.append(uj_berles)
            print(f"Sikeres berles! Bérlő: {berlo_neve} | Dátum: {datum_str}| Ár: {kivalasztott_auto.berleti_dij} Ff")
            return kivalasztott_auto.berleti_dij
        except ValueError as e:
            print(f"HIBA: {e}")
            return 0

    def berles_lemondasa(self, rendszam, datum_str, berlo_neve):
        rendszam = rendszam.upper().strip()
        datum_str = datum_str.strip()
        keresett_nev = berlo_neve.strip().lower()

        for berles in self._berlesek:
            if (berles.auto.rendszam == rendszam and
                    berles.datum == datum_str and
                    berles.berlo_neve.strip().lower() == keresett_nev):
                self._berlesek.remove(berles)
                print(f"Sikeres lemondás! A bérlés törölve.")
                return
        print("Hiba, valamelyik adat nem egyezik meg létező foglalással!")

    def berlesek_listazasa(self):
        if not self._berlesek:
            print("Nincs aktív bérlés!")
            return
        print("\n --- Bérlések listája ---")
        for berles in self._berlesek:
            print(berles.info)
