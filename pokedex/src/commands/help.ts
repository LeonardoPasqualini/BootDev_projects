import { CLICommand } from "./command.js";

export function commandHelp(commands: Record<string, CLICommand>){
  console.log("Welcome to the Pokedex!");
  console.log("Usage:");
  console.log();
  for(let key in commands) {
    console.log(`${key}: ${commands[key].description}`)
  }
  return;
}