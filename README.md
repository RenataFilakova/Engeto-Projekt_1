#  Projekt 1 – Task Manager

Tento projekt je jednoduchý konzolový správce úkolů.  
Umožňuje přidávat, zobrazovat a mazat úkoly pomocí hlavního menu.  


---

##  Funkcionalita

### 1️⃣ hlavni_menu()
- Zobrazí nabídku:
  - 1 – Přidat úkol  
  - 2 – Zobrazit úkoly  
  - 3 – Odstranit úkol  
  - 4 – Ukončit program  
- Kontroluje, zda uživatel zadal platnou volbu.

---

### 2️⃣ pridat_ukol()
- Uživatel zadává:
  - název úkolu (povinný)
  - popis úkolu (povinný)
- Úkol je uložen jako slovník do seznamu `ukoly`.
- Funkce vrací přidaný úkol.

---

### 3️⃣ zobrazit_ukoly()
- Vypíše všechny uložené úkoly.
- Pokud je seznam prázdný, zobrazí odpovídající informaci.

---

### 4️⃣ odstranit_ukol()
- Uživatel zadá číslo úkolu pro odstranění.
- Funkce kontroluje platnost indexu.
- Pokud je číslo správné, úkol je odstraněn.

---

##  Testovací scénáře
Součástí projektu je dokument **Projekt_1-Test_Cases.docx**, který obsahuje:

- pozitivní testy  
- negativní testy  
- hraniční případy  

Testy ověřují správnou funkčnost všech čtyř funkcí projektu.

---

## ▶️ Spuštění programu

V terminálu spusť:

```bash
python Projekt_1-Task_Manager.py

