let varnsdorf = 'A'
let decin = 'B'
let usti_nad_labem = 'C'
let praha = 'D'
let melnik = 'E'
let ceska_lipa = 'F'
let novy_bor = 'G'
let liberec = 'H'
let mlada_boleslav = 'J'

let mesta = [varnsdorf, decin, usti_nad_labem, praha, melnik, ceska_lipa, novy_bor, liberec, mlada_boleslav];

const adjMatrix = [
    
    [0, 44, 0, 0, 0, 0, 22, 42, 0],
    [44, 0, 25, 0, 0, 0, 0, 0, 0],
    [0, 25, 0, 93, 0, 0, 0, 0, 0],
    [0, 0, 93, 0, 34, 0, 0, 0, 67],
    [0, 0, 0, 34, 0, 0, 0, 0, 51],
    [0, 0, 0, 0, 0, 0, 10, 0, 0],
    [22, 0, 0, 0, 0, 10, 0, 0, 0],
    [42, 0, 0, 0, 0, 0, 0, 0, 48],
    [0, 0, 0, 67, 51, 0, 0, 48, 0] 
];



console.log(`        ${mesta.join('\t')}`);
for (let i = 0; i < adjMatrix.length; i++) {
  console.log(`${mesta[i]}\t${adjMatrix[i].join('\t')}`);
}

const start = 'A';
const konec = 'D';
const startX = mesta.indexOf(start);
const konecX = mesta.indexOf(konec);
const distances = cesta(adjMatrix, startX);
function cesta(adjMatrix, start) {
    const y = adjMatrix.length;
    const distance = new Array(y).fill(Infinity);
    distance[start] = 0;

    for (let i = 0; i < y - 1; i++) {
        for (let j = 0; j < y; j++) {
            for (let k = 0; k < y; k++) {
                if (adjMatrix[j][k] !== 0 && distance[j] + adjMatrix[j][k] < distance[k]) {
                    distance[k] = distance[j] + adjMatrix[j][k];
                }
            }
        }
    }

    return distance;
}


console.log("Vzdálenost od uzlu", start, "do uzlu", konec, "je", distances[konecX]);

// AB = 44
// BC = 25
// CD = 93
// DE = 34
// DI = 67
// EI = 51
// FG = 10
// AH = 42
// AG = 22
// HI = 48
