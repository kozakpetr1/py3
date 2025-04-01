# Zadání úlohy: Dilatace a eroze v 2D poli

Je dáno dvourozměrné pole `image2d` o rozměrech **9x9**. Hodnoty matice jsou v rozsahu **0 - 4**. Ve středu matice je hodnota **4**, směrem k okrajům se hodnoty budou snižovat až na **0**. Kódy pro inicializaci jsou uvedeny níže.

```
[0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 1, 1, 1, 1, 1, 1, 1, 0]
[0, 1, 2, 2, 2, 2, 2, 1, 0]
[0, 1, 2, 3, 3, 3, 2, 1, 0]
[0, 1, 2, 3, 4, 3, 2, 1, 0]
[0, 1, 2, 3, 3, 3, 2, 1, 0]
[0, 1, 2, 2, 2, 2, 2, 1, 0]
[0, 1, 1, 1, 1, 1, 1, 1, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0]
```
## Inicializace `image2d`

### Node.js (JavaScript)
```javascript
const image2d = Array.from({ length: 9 }, (_, i) =>
    Array.from({ length: 9 }, (_, j) => 4 - Math.max(Math.abs(i - 4), Math.abs(j - 4)))
);
console.log(image2d);
```

### PHP
```php
$image2d = [];
for ($i = 0; $i < 9; $i++) {
    for ($j = 0; $j < 9; $j++) {
        $image2d[$i][$j] = 4 - max(abs($i - 4), abs($j - 4));
    }
}
print_r($image2d);
```

### Python
```python
image2d = [[4 - max(abs(i - 4), abs(j - 4)) for j in range(9)] for i in range(9)]
for row in image2d:
    print(row)
```

## Popis úlohy 1
Ve vybraném jazyce proveď převod hodnot dvourozměrného pole `image2d` do markdown tabulky. Výstup přidej do dokumentace **Readme.md**.

## Popis úlohy 2
Ve vybraném jazyce Implementuj funkce `dilatace(image2d)` a `eroze(image2d)` pro provedení operací **dilatace** a **eroze** na dvourozměrném poli `image2d`.

### Požadavky:
1. **Implementace operací:**
   - **Dilatace:** Každý prvek matice se nahradí maximální hodnotou z původních sousedních hodnot (vlevo, vpravo, nad a pod).
   - **Eroze:** Každý prvek matice se nahradí minimální hodnotou z původních sousedních hodnot (vlevo, vpravo, nad a pod).

2. **Řešení lze implementovat v jazycích:**
   - Node.js (JavaScript)
   - PHP
   - Python

3. **Testování**
   - Otestuj funkčnost funkcí `dilatace(image2d)` a `eroze(image2d)` a do **Readme.md** přidej tabulku s hodnotami dvourozměrného pole po provedení **dilatace**, **eroze**, **eroze**, **dilatace** v uvedeném pořadí.
4. **Dokumentace**
   - V **Readme.md** zdokumentuj postup řešení obou úloh.

