import { createInterface } from "node:readline";
import { commandExit } from "./commands/exit.js";
import { commandHelp } from "./commands/help.js";
import { CLICommand } from "./commands/command.js";
// npm run dev | tee repl.log

export function getCommands(): Record<string, CLICommand> {
  return {
    exit: {
      name: "exit",
      description: "Exit the Pokedex",
      callback: commandExit,
    },
    help: {
      name: "help",
      description: "Displays available commands",
      callback: commandHelp,
    },
    // can add more commands here
  };
}

export function cleanInput(input: string): string[] {
  const splitArray = input.trim().split(" ");
  let cleanArr = [];
  for(let word of splitArray) {
    if (!word.length) {
      continue;
    }
    cleanArr.push(word.toLowerCase())
  }
  return cleanArr;
}

export function startREPL() {
  const rl = createInterface({
    input: process.stdin,
    output: process.stdout,
    prompt: "Pokedex > "
  });

  rl.prompt()
  rl.on("line", (line) => {
    const inputClean = cleanInput(line);

    if(inputClean.length == 0){
      rl.prompt()
      return;
    }
    // console.log(`Your command was: ${inputClean[0]}`)

    const commands = getCommands();

    switch(inputClean[0]) {
      case "exit":
        const exit = commands["exit"].callback;
        exit(commands);
      case "help":
        const help = commands["help"].callback;
        help(commands);
        break;
      default:
        console.log("Unknown command");
    }
    
    rl.prompt();
  })
}

export { CLICommand };
