import { createInterface, type Interface } from "readline";
import { commandExit } from "./commands/exit.js";
import { commandHelp } from "./commands/help.js";

export type State = {
  rl: Interface;
  commands: Record<string, CLICommand>
}

export type CLICommand = {
  name: string;
  description: string;
  callback: (state: State) => void;
};

export function initState(): State {

  const rl = createInterface({
    input: process.stdin,
    output: process.stdout,
    prompt: "Pokedex > "
  });

  const commands: Record<string, CLICommand> = {
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
  };

  return {
    rl,
    commands
  };
}