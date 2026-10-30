import { State } from "../state.js";


export async function commandPokedex(state: State, ...args: string[]) {
  if(Object.keys(state.pokedex).length === 0) {
    console.log("No pokemon caught yet.");
    return;
  };
  console.log("Your Pokedex:");
  for(let name in state.pokedex){
    console.log(`  - ${name}`);
  };

  return;
}