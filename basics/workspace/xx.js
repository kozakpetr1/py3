const matice = [
    [0, 42, 67, 0, 0, 0, 90, 0, 0], // Praha
    [42, 0, 41, 0, 0, 0, 0, 55, 0], // Mělník
    [67, 41, 0, 51, 0, 0, 0, 44, 0], // Mladá Boleslav
    [0, 0, 51, 0, 42, 0, 0, 0, 0], // Liberec
    [0, 0, 0, 42, 0, 44, 0, 0, 22], // Varnsdorf
    [0, 0, 0, 0, 44, 0, 25, 0, 30], // Děčín
    [90, 0, 0, 0, 0, 25, 0, 0, 0], // Ústí nad Labem
    [0, 55, 44, 0, 0, 0, 0, 0, 10], // Česká Lípa
    [0, 0, 0, 0, 22, 30, 0, 10, 0], // Nový Bor
];

const mesta = {
    "Praha": 0,
    "Mělník": 1,
    "Mladá Boleslav": 2,
    "Liberec": 3,
    "Varnsdorf": 4,
    "Děčín": 5,
    "Ústí nad Labem": 6,
    "Česká Lípa": 7,
    "Nový Bor": 8
};

function najdiCestu(start, cil) {

    const startIndex = typeof start === 'string' ? mesta[start] : start;
    const cilIndex = typeof cil === 'string' ? mesta[cil] : cil;
    const pocetMest = matice.length;
    
    const vzdalenosti = new Array(pocetMest).fill(Infinity);
    const predchudci = new Array(pocetMest).fill(-1);
    const navstiveno = new Array(pocetMest).fill(false);
    
    vzdalenosti[startIndex] = 0;
    
    for (let i = 0; i < pocetMest; i++) {
        let min = Infinity;
        let minIndex = -1;
        
        for (let j = 0; j < pocetMest; j++) {
            if (!navstiveno[j] && vzdalenosti[j] < min) {
                min = vzdalenosti[j];
                minIndex = j;
            }
        }
        
        if (minIndex === -1) break;
        
        navstiveno[minIndex] = true;
        
        if (minIndex === cilIndex) break;
        
        for (let j = 0; j < pocetMest; j++) {
        if (matice[minIndex][j] > 0) {
                const novaVzdalenost = vzdalenosti[minIndex] + matice[minIndex][j];
        
                if (novaVzdalenost < vzdalenosti[j]) {
                    vzdalenosti[j] = novaVzdalenost;
                    predchudci[j] = minIndex;
                }
            }
        }
    }
    
    
    if (vzdalenosti[cilIndex] === Infinity) {
        return { 
            cesta: null, 
            delka: -1, 
            zprava: "Cesta mezi zadanými městy neexistuje!" 
        };
    }
    
    const cesta = [];
    let aktualniIndex = cilIndex;
    
    while (aktualniIndex !== -1) {
        cesta.unshift(aktualniIndex);
        aktualniIndex = predchudci[aktualniIndex];
    }
    
    return prevedCestuNaNazvy(cesta, vzdalenosti[cilIndex]);
}

function prevedCestuNaNazvy(cesta, delka) {
    const nazvy = cesta.map(index => {
        for (const mesto in mesta) {
            if (mesta[mesto] === index) {
                return mesto;
            }
        }
        return `Neznámé město (${index})`;
    });
    
    return {
        cesta: nazvy,
        delka: delka,
        zprava: `Nalezena nejkratší cesta z ${nazvy[0]} do ${nazvy[nazvy.length - 1]} o délce ${delka} km.`
    };
}

const startMesto = "Praha";
const cilMesto = "Nový Bor";
const vysledek = najdiCestu(startMesto, cilMesto);

console.log(vysledek.zprava);
console.log("Cesta:", vysledek.cesta.join(" -> "));
console.log("Celková délka:", vysledek.delka, "km");