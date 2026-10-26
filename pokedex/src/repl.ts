import { createInterface } from "node:readline";
import { commandExit } from "./commands/exit.js";
import { commandHelp } from "./commands/help.js";
import { CLICommand, State } from "./state.js";
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

export function startREPL(state: State) {
  const rl = state.rl

  rl.prompt()
  rl.on("line", (line) => {
    const inputClean = cleanInput(line);

    if(inputClean.length == 0){
      rl.prompt()
      return;
    }
    // console.log(`Your command was: ${inputClean[0]}`)

    const commands = state.commands;

    switch(inputClean[0]) {
      case "exit":
        commandExit(state);
      case "help":
        commandHelp(state);
        break;
      default:
        console.log("Unknown command");
    }
    
    rl.prompt();
  })
}

export { CLICommand };
