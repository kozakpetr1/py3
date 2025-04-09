const prompt = require("prompt-sync")();
let instructions = "ezop I@G@++O@-O@#";
let value = 0;

function ezop(ins) {
  let split = ins.split(" ");
  if (split[0] !== "ezop" || split.length !== 2) {
    console.log("Nespárvná instrukce");
    return;
  }
  let instruction = split[1].split("");
  console.log(instruction);
  let v = 0;

  for (let i = 0; i < instruction.length; i++) {
    switch (instruction[i]) {
      case "I":
        if (instruction[i + 1] === "@") {
          i++;
          v = parseInt(prompt("Zadejte hodnotu: "));
        } else {
          console.log("Nespárvná instrukce");
          return;
        }
        break;
      case "G":
        if (instruction[i + 1] === "@") {
          i++;
          v = Math.floor(Math.random() * 2048) - 1024;
        } else {
          console.log("Nespárvná instrukce");
          return;
        }

        break;
      case "O":
        if (instruction[i + 1] === "@") {
          console.log(v);
          i++;
        } else {
          console.log("Nespárvná instrukce");
          return;
        }

        break;
      case "+":
        v++;
        break;
      case "-":
        v--;
        break;
      case "#":
        console.log("Skript ukončen.");
        return v;
      default:
        console.log("Nespárvná instrukce");
        return;
    }
  }
}

ezop(instructions);