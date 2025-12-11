from typing import List, Dict, Optional

ukoly: List[Dict[str, str]] = []


def pridat_ukol(nazev: Optional[str] = None, popis: Optional[str] = None) -> int:
    while True:
        if nazev is None:
            nazev = input("Zadejte název úkolu: ").strip()
        if not nazev:
            print(" Chyba: Název úkolu nesmí být prázdný. Zkuste to znovu.\n")
            nazev = None
            continue

        if popis is None:
            popis = input("Zadejte popis úkolu: ").strip()
        if not popis:
            print(" Chyba: Popis úkolu nesmí být prázdný. Zkuste to znovu.\n")
            popis = None
            continue

        ukoly.append({"nazev": nazev, "popis": popis})
        idx = len(ukoly)
        print(f" Úkol '{nazev}' byl úspěšně přidán.\n")
        return idx


def zobrazit_ukoly() -> None:
    if not ukoly:
        print(" Seznam úkolů je prázdný.\n")
        return

    print("\nÚKOLY:")
    for i, ukol in enumerate(ukoly, start=1):
        print(f" {i}. {ukol['nazev']} – {ukol['popis']}")
    print("")


def odstranit_ukol(index: Optional[int] = None) -> bool:
    if not ukoly:
        print(" Seznam úkolů je prázdný, není co odstranit.\n")
        return False

    while True:
        if index is None:
            vstup = input("Zadejte číslo úkolu k odstranění: ").strip()
            if not vstup.isdigit():
                print(" Zadejte prosím platné číslo.\n")
                continue
            index = int(vstup)

        if index < 1 or index > len(ukoly):
            print(" Úkol s tímto číslem neexistuje.\n")
            return False

        odstraneny = ukoly.pop(index - 1)
        print(f" Úkol '{odstraneny['nazev']}' byl odstraněn.\n")
        return True


def hlavni_menu() -> None:
    while True:
        print("=== Task Manager ===")
        print("1. Přidat úkol")
        print("2. Zobrazit úkoly")
        print("3. Odstranit úkol")
        print("4. Ukončit program")

        volba = input("Vyberte možnost (1–4): ").strip()

        if volba == "1":
            pridat_ukol()
        elif volba == "2":
            zobrazit_ukoly()
        elif volba == "3":
            odstranit_ukol()
        elif volba == "4":
            print(" Konec programu.")
            break
        else:
            print(" Neplatná volba. Zadejte prosím číslo 1–4.\n")


if __name__ == "__main__":
    try:
        hlavni_menu()
    except KeyboardInterrupt:
        print("\nProgram ukončen uživatelem.")
