import { createInterface, type Interface } from "readline";
import { commandExit } from "./commands/exit.js";
import { commandHelp } from "./commands/help.js";
import { commandMap, commandMapB } from "./commands/map.js";
import { PokeAPI, Pokemon } from "./pokeapi.js";
import { commandExplore } from "./commands/explore.js";
import { commandCatch } from "./commands/catch.js";
import { commandInspect } from "./commands/inspect.js";

export type State = {
  rl: Interface;
  commands: Record<string, CLICommand>;
  pokeAPI: PokeAPI;
  nexLocationURL: string | null;
  prevLocationURL: string | null;
  pokedex: Record<string, Pokemon>;
}

export type CLICommand = {
  name: string;
  description: string;
  callback: (state: State, ...args: string[]) => Promise<void>;
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
    },
    explore: {
      name: "explore <area name>",
      description: "Display the pokemons found in the given area.",
      callback: commandExplore,
    },
    catch: {
      name: "catch <pokemon>",
      description: "Tries to catch a pokemon by it's name. The chances are based on the pokemon's exp",
      callback: commandCatch,
    },
    inspect: {
      name: "inspect <pokemon>",
      description: "Inspect the details of a pokemon you caught.",
      callback: commandInspect,
    }
  };

  const pokeAPI = new PokeAPI();

  return {
    rl,
    commands,
    pokeAPI,
    nexLocationURL: null,
    prevLocationURL: null,
    pokedex: {}
  };
}