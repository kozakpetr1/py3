## Zadání úlohy: Výpočet obsahu plochy pod parabolou

### Cíl
Vaším úkolem je implementovat program (Python, PHP nebo node.js), který vypočítá obsah plochy pod parabolou \( y = ax^2 + bx + c \) v zadaném intervalu <x1, x2>.

### Zadání
1. **Analýza funkce**
   - Zadaná funkce představuje kvadratickou parabolu, která leží nad osou \( x \).
   - Obsah plochy pod křivkou v daném intervalu lze spočítat pomocí určitého integrálu.

2. **Implementace**
   - Implementujte funkci, která:
     - Přijme koeficienty kvadratické funkce \( a, b, c \) a krajní body intervalu \( x1, x2 \).
     - Vypočítá obsah plochy pod křivkou v tomto intervalu pomocí určitého integrálu.
     - Vrátí absolutní hodnotu tohoto obsahu.

### Výstup
Váš program by měl obsahovat pouze výpočet integrálu a výpis výsledku, například:

#### Python:
```python
def parabola_area(a, b, c, x1, x2):
    """
    Vypočítá obsah plochy pod parabolou y = ax^2 + bx + c v intervalu <x1, x2>.
    """
    pass

# Příklad použití:
a, b, c = 1, 0, 0  # y = x^2
x1, x2 = 0, 2

area = parabola_area(a, b, c, x1, x2)
print(f"Obsah plochy pod parabolou v intervalu <{x1}, {x2}> je {area}")
```
