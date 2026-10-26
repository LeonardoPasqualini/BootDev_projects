import { createInterface, type Interface } from "readline";
import { commandExit } from "./commands/exit.js";
import { commandHelp } from "./commands/help.js";
import { commandMap, commandMapB } from "./commands/commandMap.js";
import { PokeAPI } from "./pokeapi.js";

export type State = {
  rl: Interface;
  commands: Record<string, CLICommand>;
  pokeAPI: PokeAPI;
  nexLocationURL: string | undefined;
  prevLocationURL: string | undefined;
}

export type CLICommand = {
  name: string;
  description: string;
  callback: (state: State) => Promise<void>;
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
    map: {
      name: "map",
      description: "Display names of 20 location areas in the Pokemon world. Each subsequent call to the map command will display the next 20 locations.",
      callback: commandMap,
    },
    mapb: {
      name: "mapb",
      description: "Display previous names of 20 location areas in the Pokemon world. Each subsequent call to the mapb command will display the previous 20 locations.",
      callback: commandMapB,
    }
  };

  const pokeAPI = new PokeAPI();

  return {
    rl,
    commands,
    pokeAPI,
    nexLocationURL: undefined,
    prevLocationURL: undefined,
  };
}