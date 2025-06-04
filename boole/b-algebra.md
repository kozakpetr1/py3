# Úvod do Booleovy algebry
https://www.youtube.com/watch?v=kI38tmzI7JM

## Co je Booleova algebra?

Booleova algebra je způsob, jak pracovat s logickými hodnotami: **pravda (1)** a **nepravda (0)**.  
Využívá se hlavně v **informatice**, **elektrotechnice** a **logice** – například při návrhu digitálních obvodů nebo při programování podmínek.

---

## Základní hodnoty

Booleova algebra používá pouze dvě hodnoty:

- `1` – pravda (true)
- `0` – nepravda (false)

---

## Základní logické operace

### 1. AND – logický součin (`∧`, `·`)

Výsledek je `1`, jen když **oba vstupy jsou 1**.

| A | B | A ∧ B |
|---|---|--------|
| 0 | 0 |   0    |
| 0 | 1 |   0    |
| 1 | 0 |   0    |
| 1 | 1 |   1    |

---

### 2. OR – logický součet (`∨`, `+`)

Výsledek je `1`, když **alespoň jeden vstup je 1**.

| A | B | A ∨ B |
|---|---|--------|
| 0 | 0 |   0    |
| 0 | 1 |   1    |
| 1 | 0 |   1    |
| 1 | 1 |   1    |

---

### 3. NOT – negace (`¬A`, `A′`)

Výsledek je opačný než vstupní hodnota.

| A | ¬A |
|---|----|
| 0 |  1 |
| 1 |  0 |

---

### 4. XOR – exkluzivní OR (`⊕`)

Výsledek je `1`, **pokud je právě jeden vstup 1** (ne oba).

| A | B | A ⊕ B |
|---|---|--------|
| 0 | 0 |   0    |
| 0 | 1 |   1    |
| 1 | 0 |   1    |
| 1 | 1 |   0    |

**Přirovnání:** „Buď A, nebo B – ale ne oba.“

---

### 5. Ekvivalence – logická rovnost (`≡`, `↔`)

Výsledek je `1`, když jsou **oba vstupy stejné**.

| A | B | A ≡ B |
|---|---|--------|
| 0 | 0 |   1    |
| 0 | 1 |   0    |
| 1 | 0 |   0    |
| 1 | 1 |   1    |

💡 **Přirovnání:** „Obě podmínky dávají stejný výsledek.“

---

## Příklady z praxe

- **AND:** Dveře se otevřou, když je zadán správný kód **a zároveň** stisknuto tlačítko.
- **OR:** Zapne se výstražné světlo, když je aktivní **libovolný senzor**.
- **NOT:** Pokud není detekován pohyb, **aktivuj alarm**.
- **XOR:** Světlo ovládané dvěma spínači – **zapne se, když je jen jeden spínač zapnutý**.
- **Ekvivalence:** Zkontroluj, že **dva přepínače jsou ve stejné poloze**.

---

## Příklady booleovských výrazů

Vyhodnoť výstup daných logických výrazů pro všechny možné kombinace hodnot A, B a C (0 nebo 1).

---

### Příklad 1:  
**Výraz:** `(A ∧ B) ∨ C`

| A | B | C | (A ∧ B) ∨ C |
|---|---|---|--------------|
| 0 | 0 | 0 |       0      |
| 0 | 0 | 1 |       1      |
| 0 | 1 | 0 |       0      |
| 0 | 1 | 1 |       1      |
| 1 | 0 | 0 |       0      |
| 1 | 0 | 1 |       1      |
| 1 | 1 | 0 |       1      |
| 1 | 1 | 1 |       1      |

---

### Příklad 2:  
**Výraz:** `¬A ∨ (B ∧ C)`

| A | B | C | ¬A | B ∧ C | ¬A ∨ (B ∧ C) |
|---|---|---|----|--------|---------------|
| 0 | 0 | 0 | 1  |   0    |      1        |
| 0 | 0 | 1 | 1  |   0    |      1        |
| 0 | 1 | 0 | 1  |   0    |      1        |
| 0 | 1 | 1 | 1  |   1    |      1        |
| 1 | 0 | 0 | 0  |   0    |      0        |
| 1 | 0 | 1 | 0  |   0    |      0        |
| 1 | 1 | 0 | 0  |   0    |      0        |
| 1 | 1 | 1 | 0  |   1    |      1        |

---

### Příklad 3:  
**Výraz:** `(A ⊕ B) ∧ C`

| A | B | C | A ⊕ B | Výsledek |
|---|---|---|--------|-----------|
| 0 | 0 | 0 |   0    |    0      |
| 0 | 0 | 1 |   0    |    0      |
| 0 | 1 | 0 |   1    |    0      |
| 0 | 1 | 1 |   1    |    1      |
| 1 | 0 | 0 |   1    |    0      |
| 1 | 0 | 1 |   1    |    1      |
| 1 | 1 | 0 |   0    |    0      |
| 1 | 1 | 1 |   0    |    0      |

---

### Příklad 4:  
**Výraz:** `(A ≡ B) ∨ ¬C`

| A | B | C | A ≡ B | ¬C | Výsledek |
|---|---|---|--------|----|-----------|
| 0 | 0 | 0 |        |    |           |
| 0 | 0 | 1 |        |    |           |
| 0 | 1 | 0 |        |    |           |
| 0 | 1 | 1 |        |    |           |
| 1 | 0 | 0 |        |    |           |
| 1 | 0 | 1 |        |    |           |
| 1 | 1 | 0 |        |    |           |
| 1 | 1 | 1 |        |    |           |

---

**Úkol pro žáky:** Doplňte do tabulek mezivýpočty a výsledky. Dokázali byste nakreslit jednoduchý logický obvod podle výrazů?

