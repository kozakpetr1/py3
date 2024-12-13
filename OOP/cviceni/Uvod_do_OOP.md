### Zadání: OOP v Pythonu

Níže je pět různých úloh zaměřených na různé aspekty objektově orientovaného programování (OOP) v Pythonu. Při řešení se zaměřte na čistý a přehledný kód a dodržování zásad OOP.

---

#### **Úloha 1: Správa knihovny (skládání v OOP)**  
Navrhněte a implementujte třídy pro správu knihovny:  
1. Vytvořte třídu `Kniha`, která bude obsahovat atributy jako název, autor a počet stran.  
2. Vytvořte třídu `Knihovna`, která bude obsahovat seznam knih. Tato třída bude mít metody:  
   - `pridej_knihu(kniha)`: přidá knihu do knihovny,  
   - `odeber_knihu(nazev)`: odebere knihu podle názvu,  
   - `zobraz_knihy()`: vypíše všechny knihy v knihovně.  
3. V programu otestujte přidávání a odebírání knih pomocí skládání objektů.  

---

#### **Úloha 2: Fluentní interface – Správa objednávek**  
Implementujte třídu `Objednavka`, která umožňuje sestavování objednávky pomocí fluentního rozhraní:  
1. Třída bude mít atributy pro jméno zákazníka, seznam položek a cenu.  
2. Implementujte metody:  
   - `nastav_zakaznika(jmeno)`: nastaví jméno zákazníka,  
   - `pridej_polozku(polozka, cena)`: přidá položku do objednávky,  
   - `vypis_objednavku()`: vypíše detaily objednávky.  
3. Zajistěte, aby každá metoda vracela instanci třídy, což umožní řetězení volání, např.:  
   ```python
   objednavka = Objednavka().nastav_zakaznika("Jan Novák").pridej_polozku("Kniha", 200).pridej_polozku("Pero", 20)
   objednavka.vypis_objednavku()
   ```

---

#### **Úloha 3: Abstraktní třídy a metody – Zvířata v ZOO**  
1. Vytvořte abstraktní třídu `Zivocich` s následujícími abstraktními metodami:  
   - `ozvi_se()`: každý živočich musí mít vlastní způsob, jak se ozývá,  
   - `pohybuj_se()`: každý živočich musí mít vlastní způsob pohybu.  
2. Odvoďte konkrétní třídy `Lev`, `Orel` a `Ryba`, které implementují tyto metody.  
3. Vytvořte instanci každého živočicha a demonstrujte, jak se ozývá a pohybuje. Použijte moduly `abc` a `ABC` v Pythonu.  

---

#### **Úloha 4: Skladový systém (skládání a polymorfismus)**  
1. Vytvořte třídu `Produkt`, která bude mít atributy název a cena.  
2. Vytvořte třídu `Sklad`, která bude obsahovat seznam produktů a metody:  
   - `pridej_produkt(produkt)`: přidá produkt do skladu,  
   - `zobraz_produkty()`: vypíše všechny produkty ve skladu.  
3. Přidejte specializovanou třídu `Potravina`, která dědí od `Produkt` a přidává atribut `datum_spotreby`.  
4. Umožněte správu potravin ve skladu s kontrolou data spotřeby.  

---

#### **Úloha 5: Hierarchie vozidel (abstraktní třídy a dědičnost)**  
1. Vytvořte abstraktní třídu `Vozidlo` s atributy jako značka, model a abstraktní metodou `start()`.  
2. Implementujte třídy `Auto` a `Motorka`, které dědí z třídy `Vozidlo`.  
   - Třída `Auto` bude mít atribut `pocet_dveri` a implementaci metody `start()` s hláškou: *"Auto {značka} startuje se {počet_dveri} dveřmi."*  
   - Třída `Motorka` bude mít atribut `typ_motorky` a metodu `start()` s hláškou: *"Motorka {značka} typu {typ_motorky} startuje."*  
3. Ověřte funkčnost pomocí několika instancí obou tříd.  

---

### Pokyny k odevzdání:  
1. Vyberte si jednu z úloh.  
2. Implementujte řešení v Pythonu.  
3. Kód uložte do souboru pojmenovaného dle formátu: `jmeno_prijmeni_ulohaX.py`.  
4. Odevzdejte vypracování na platformě pro sdílení úkolů do termínu: **[doplňte datum]**.
