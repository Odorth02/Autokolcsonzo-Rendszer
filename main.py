from jarmuvek import Szemelyauto, Teherauto
from kolcsonzo import Autokolcsonzo

def autok_beolvasasa(kolcsonzo, faljnev="autolista.txt"):
    try:
        with open(faljnev, "r", encoding="utf=8") as fajl:
            for sor in fajl:
                sor = sor.strip()
                if not sor:
                    continue
                adatok = sor.split(",")
                if len(adatok) < 5:
                    continue

                jarmu_fajta = adatok[0].strip().lower()
                rendszam = adatok[1].strip()
                tipus = adatok[2].strip()
                berleti_dij = int(adatok[3].strip())
                egyedi_ertek = int(adatok[4].strip())

                if jarmu_fajta == "szemelyauto":
                    auto = Szemelyauto(rendszam, tipus, berleti_dij, egyedi_ertek)
                    kolcsonzo.auto_hozzaadas(auto)
                elif jarmu_fajta == "teherauto":
                    auto = Teherauto(rendszam, tipus, berleti_dij, egyedi_ertek)
                    kolcsonzo.auto_hozzaadas(auto)
    except FileNotFoundError:
        print(f"Fálj nem található")
    except Exception as e:
        print(f"Hiba: {e}")


def main():
    kolcsonzo = Autokolcsonzo("X6NQFU Autokölcsönző")
    autok_beolvasasa(kolcsonzo, "autolista.txt")
#tesztkölcsönzések
    kolcsonzo.auto_berles("ABC-123","2026-10-01","Nagy Péter")
    kolcsonzo.auto_berles("XYZ-789","2026-10-02","Kis Lajos")
    kolcsonzo.auto_berles("DEF-456","2026-10-03","Tóth Sándor")
    kolcsonzo.auto_berles("ABC-123","2026-10-04","Kovács Géza")

    while True:
        print(f"\n ---{kolcsonzo.nev} MENÜ ---")
        print("1. Autók listázása")
        print("2. Autó bérlés")
        print("3. Bérlés lemondása")
        print("4. Bérlések listázása")
        print("5. Kilépés")

        valasztas = input("Válasszon menüpontot (1-5):").strip()

        if valasztas == "1":
            kolcsonzo.autok_listazasa()
        elif valasztas == "2":
            print("\n--- Autó bérlése ---")
            rendszam = input("Addja meg az autó rendszámát: ").strip()
            datum = input("Addja meg a berlés dátumt (ÉÉÉÉ-HH-NN): ").strip()
            nev = input("Addja meg a nevét: ").strip()
            kolcsonzo.auto_berles(rendszam, datum, nev)
        elif valasztas == "3":
            print("\n--- Bérlés lemondása ---")
            rendszam = input("Addja meg az autó rendszámát: ").strip()
            datum = input("Addja meg a berlés dátumt (ÉÉÉÉ-HH-NN): ").strip()
            nev = input("Addja meg a nevét: ").strip()
            kolcsonzo.berles_lemondasa(rendszam, datum, nev)
        elif valasztas == "4":
            kolcsonzo.berlesek_listazasa()
        elif valasztas == "5":
            print("Viszlát!")
            break
        else:
            print("Kérjük 1 és 5 közötti számot adjon meg!")

if __name__ == "__main__":
    main()
