<?php

// ---------------------------------------------------------------------
// Třída Character – obecný charakter (postava) v počítačové hře
// ---------------------------------------------------------------------
class Character
{
    /*
     * Statická vlastnost třídy – společná pro všechny instance.
     * Obsahuje seznam přípustných rolí, které může postava mít.
     * Přístup: Character::$roles
     */
    public static $roles = [
        "obchodník",
        "strážce",
        "léčitel",
        "válečník",
        "druid",
        "čaroděj",
        "vědmák"
    ];

    // Soukromé vlastnosti objektu – nelze je měnit přímo zvenčí.
    private $name;   // jméno postavy
    private $role;   // role postavy (musí být z pole $roles, jinak null)

    /*
     * Konstruktor – speciální metoda, volá se automaticky při vytvoření objektu.
     * Slouží k inicializaci (nastavení) vlastností nového objektu.
     *
     * Parametry:
     *  - $name : jméno postavy
     *  - $role : požadovaná role postavy
     */
    public function __construct($name, $role)
    {
        // uložíme zadané jméno
        $this->name = $name;

        // zkontrolujeme, jestli je zadaná role povolená
        // in_array($role, self::$roles) vrátí true, pokud $role existuje v poli $roles
        if (in_array($role, self::$roles)) {
            $this->role = $role;
        } else {
            // pokud role není povolená, uložíme null (žádná platná role)
            $this->role = null;
        }
    }

    /*
     * Destruktor – speciální metoda, volá se automaticky při zániku objektu.
     * V PHP  je to typicky ve chvíli, kdy:
     *  - skript končí
     *  - nebo výslovně zavoláme unset($objekt)
     *
     * Zde pouze vypíšeme informaci, že byla postava odstraněna ze hry.
     */
    public function __destruct()
    {
        echo "Postava {$this->name} byla odstraněna ze hry.\n";
    }

    /*
     * Magická metoda __toString()
     *  - definuje textovou reprezentaci objektu
     *  - PHP tuto metodu samo zavolá, když se objekt použije jako text
     *    např. při echo $objekt;
     *
     * Vrací krátký popis postavy (role + jméno).
     */
    public function __toString()
    {
        return "Role: {$this->role}, Jméno: {$this->name}";
    }
}

// ---------------------------------------------------------------------
// Třída PlayerCharacter – postava ovládaná hráčem
// Dědí (extends) třídu Character, proto má všechny její vlastnosti a metody.
// ---------------------------------------------------------------------
class PlayerCharacter extends Character
{
    // Další vlastnost popisující, jak je postava ovládána (např. klávesnice, gamepad…)
    private $device;

    /*
     * Konstruktor PlayerCharacter
     *
     * Parametry:
     *  - $name          : jméno postavy
     *  - $role          : role postavy (validuje se v rodičovském konstruktoru)
     *  - $controlDevice : způsob ovládání (např. "klávesnice", "gamepad")
     *
     * Nejprve zavoláme konstruktor rodičovské třídy pomocí parent::__construct(),
     * abychom nastavili jméno a roli stejně jako u běžné postavy.
     * Poté nastavíme vlastní vlastnost $device.
     */
    public function __construct($name, $role, $controlDevice)
    {
        // volání konstruktoru rodiče (třídy Character)
        parent::__construct($name, $role);

        // nastavení způsobu ovládání pro tuto postavu
        $this->device = $controlDevice;
    }

    /*
     * Přetížení (přepsání) metody __toString() z rodičovské třídy.
     * Chceme zobrazit stejné informace jako u Character PLUS
     * navíc informaci o ovládání postavy.
     *
     * Pomocí parent::__toString() si vyžádáme text z rodičovské třídy
     * a jen k němu přidáme další text.
     */
    public function __toString()
    {
        return parent::__toString() . ", Ovládání: {$this->device}";
    }
}

// ---------------------------------------------------------------------
// Vytvoření objektů a ukázka práce s třídami
// ---------------------------------------------------------------------

// Vytvoříme nehráčskou postavu (NPC) – instanci třídy Character
$npc_character = new Character("Stregobor", "čaroděj");

// Vytvoříme hráčskou postavu – instanci třídy PlayerCharacter
$zaklinac = new PlayerCharacter("Zaklínač", "vědmák", "klávesnice");

// echo automaticky zavolá metodu __toString() na objektech
echo $npc_character . "\n";
echo $zaklinac . "\n";

// Výslovné zrušení objektů – vyvolá se destruktor __destruct()
// (jinak by se zavolal automaticky na konci skriptu)
unset($npc_character);
unset($zaklinac);
