# Zadání úlohy: Interpret ezoterického programovacího jazyka

## Popis úlohy
Tvým úkolem je implementovat jednoduchý interpret ezoterického programovacího jazyka `ezop`, který podporuje následující sadu příkazů:

- `I@`, `G@`, `O@`, `+`, `-`, `0`, `#`

Interpret bude spouštěn následovně
```
ezop I@++O@-O@#
```
případně takto
```
ezop "I@++O@-O@#"
```
### Požadavky:
1. **Implementace interpretu**
   - Program bude číst vstupní instrukce v textovém formátu.
   - Instrukce budou zadávány přes parametr příkazového řádku a budou uloženy do fronty FIFO.
   - Program bude postupně vybírat a vykonávat instrukce z fronty.
   - V případě, že nebude zápis syntakticky správný (např. `IO@`), zobrazí se chybové hlášení a skript bude ukončen.
   - Počáteční hodnota proměnné `@` je před interpretací příkazů inicializována vždy na 0.
   
2. **Podpora příkazů:**
   - `I@` - Načte celočíselnou hodnotu ze standardního vstupu a uloží ji do proměnné `@`.
   - `G@` - Vygeneruje pseudonáhodné celé číslo o rozsahu -1024 .. 1024 a uloží do proměnné `@`.
   - `O@` - Vypíše hodnotu proměnné `@` na standardní výstup.
   - `+` - Inkrementuje hodnotu proměnné `@` o 1.
   - `-` - Dekrementuje hodnotu proměnné `@` o 1.
   - `0` - Nastaví hodnotu proměnné `@` na 0.
   - `#` - Ukončí interpretaci a zobrazí hlášku o ukončení skriptu.

3. **Řešení lze implementovat v jazycích:**
   - Node.js (JavaScript)
   - PHP
   - Python

---

## Příklad vstupního programu

```
ezop I@++O@-O@#
```

### Očekávaný výstup (při zadání `@ = 5`):
```
7
6
Skript ukončen.
```

---

## Doporučené kroky
1. Implementuj interpret, který bude zpracovávat výše uvedené příkazy z fronty FIFO.
2. Otestuj výstupy na různých vstupních hodnotách.
3. Ujisti se, že interpret správně pracuje s proměnnou `@` a provádí operace podle zadání.


