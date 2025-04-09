Ahoj! Jasně, tady je návrh úlohy pro maturanty rozdělený na dvě části, zaměřený na práci s dvourozměrným polem (listem). Zadání je univerzální, aby se dalo snadno implementovat v Pythonu, PHP i Node.js.

---

## 🧩 **Název úlohy: Analýza tabulky prodeje**

### 🧠 Úloha 1 – Načtení a základní zpracování dat

Máme tabulku s údaji o denních tržbách pěti obchodníků za sedm dní. Tabulka je reprezentována jako dvourozměrné pole (list/list of lists), kde každý řádek představuje jednoho obchodníka a každý sloupec odpovídá jednomu dni (pondělí až neděle).

Příklad vstupních dat:
```plaintext
[
  [1200, 1350, 1100, 1600, 1800, 1750, 1900],
  [1000, 950, 1200, 1100, 1050, 1300, 1400],
  [1500, 1450, 1600, 1700, 1750, 1650, 1800],
  [900, 850, 800, 950, 1000, 1050, 1100],
  [1300, 1250, 1350, 1400, 1450, 1500, 1550]
]
```

#### Zadání:
1. Načti uvedená data do vhodné datové struktury.
2. Vypočítej celkovou tržbu každého obchodníka za týden.
3. Vypiš obchodníka s nejvyšší týdenní tržbou a částku, kterou utržil.

---

### 🔧 Úloha 2 – Rozšířená analýza

#### Zadání:
1. Vypočítej průměrnou denní tržbu všech obchodníků (pro každý den samostatně – tedy sedm hodnot).
2. Najdi den, ve kterém byl celkový obrat nejvyšší, a vypiš jeho index (0 pro pondělí, 6 pro neděli).
3. Uprav původní tabulku tak, že každý prvek (tržba) bude nahrazen hodnotou:
   - `"N"` pokud byla tržba **nižší** než průměrná tržba toho obchodníka za celý týden,
   - `"P"` pokud byla tržba **průměrná nebo vyšší** než průměrná tržba obchodníka.

---
