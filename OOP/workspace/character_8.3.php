<?php
// Přísný režim typů – PHP bude hlídat datové typy argumentů a návratových hodnot.
declare(strict_types=1);

// ---------------------------------------------------------------------
// Třída Character – obecný charakter (postava) v počítačové hře
// ---------------------------------------------------------------------
class Character
{
    /*
     * Konstanta třídy – seznam povolených rolí.
     * Na rozdíl od proměnných je konstanta neměnná (nelze ji změnit za běhu).
     * Přístup: Character::ROLES
     */
    public const ROLES = [
        "obchodník",
        "strážce",
        "léčitel",
        "válečník",
        "druid",
        "čaroděj",
        "vědmák"
    ];

    /*
     * readonly vlastnost znamená:
     *  - lze ji nastavit pouze v konstruktoru (nebo při deklaraci),
     *  - po vytvoření objektu už ji nelze změnit.
     *
     * Typová deklarace `string` určuje, že $name MUSÍ být řetězec.
     */
    private readonly string $name;

    /*
     * Typ `?string` znamená "string NEBO null".
     * Použijeme ho v případě, že roli nemusíme mít platnou (např. špatně zadaná role).
     */
    private ?string $role;

    /*
     * Konstruktor – spustí se automaticky při vytvoření instance třídy (new Character(...)).
     *
     * Deklarace:
     *  - string $name  → argument musí být řetězec
     *  - string $role  → argument musí být řetězec
     */
    public function __construct(string $name, string $role)
    {
        // readonly vlastnost nastavíme v konstruktoru
        $this->name = $name;

        // in_array() s třetím parametrem true provádí "strict" porovnávání (===)
        if (in_array($role, self::ROLES, true)) {
            $this->role = $role;
        } else {
            // pokud role není platná, uložíme null
            $this->role = null;
        }
    }

    /*
     * Destruktor – volá se při zániku objektu (na konci skriptu
     * nebo při unset($objekt)).
     *
     * Pouze vypíšeme zprávu, že postava byla odstraněna ze hry.
     */
    public function __destruct()
    {
        echo "Postava {$this->name} byla odstraněna ze hry.\n";
    }

    /*
     * Magická metoda __toString()
     *
     * - definuje, jak se objekt převede na řetězec.
     * - v deklaraci uvádíme návratový typ `: string`,
     *   což znamená, že metoda VŽDY vrací řetězec.
     */
    public function __toString(): string
    {
        return "Role: {$this->role}, Jméno: {$this->name}";
    }
}

// ---------------------------------------------------------------------
// Třída PlayerCharacter – postava ovládaná hráčem
// Dědí (extends) třídu Character, takže má její vlastnosti i metody.
// ---------------------------------------------------------------------
class PlayerCharacter extends Character
{
    /*
     * readonly string $device – textová informace o způsobu ovládání postavy
     * (např. "klávesnice", "gamepad", "myš + klávesnice"…)
     */
    private readonly string $device;

    /*
     * Konstruktor PlayerCharacter
     *
     * Parametry:
     *  - string $name          : jméno postavy
     *  - string $role          : role postavy (ověří se v konstruktoru rodiče)
     *  - string $controlDevice : způsob ovládání
     *
     * První krok: zavoláme konstruktor rodiče (Character) pomocí parent::__construct().
     * Druhý krok: uložíme vlastní vlastnost $device.
     */
    public function __construct(string $name, string $role, string $controlDevice)
    {
        parent::__construct($name, $role);
        $this->device = $controlDevice;
    }

    /*
     * Přepis (override) metody __toString() z rodičovské třídy.
     *
     * Signatura MUSÍ být stejná jako v rodiči:
     *  - název metody
     *  - počet a typy parametrů
     *  - návratový typ : string
     *
     * Pomocí parent::__toString() získáme text z rodičovské verze
     * a jen k němu přidáme informaci o způsobu ovládání.
     */
    public function __toString(): string
    {
        return parent::__toString() . ", Ovládání: {$this->device}";
    }
}

// ---------------------------------------------------------------------
// Vytvoření objektů a ukázka použití
// ---------------------------------------------------------------------

// Nehráčská postava (NPC) – instance třídy Character
$npcCharacter = new Character("Stregobor", "čaroděj");

// Hráčská postava – instance třídy PlayerCharacter
$zaklinac = new PlayerCharacter("Zaklínač", "vědmák", "klávesnice");

// echo na objekt → PHP automaticky zavolá __toString()
echo $npcCharacter . "\n";
echo $zaklinac . "\n";

// Explicitní zrušení objektů – vyvolá se destruktor __destruct()
// (jinak by se zavolal automaticky na konci skriptu)
unset($npcCharacter);
unset($zaklinac);
