import { Encounter, Pokemon } from "../pokeapi.js";
import { State } from "../state.js";


export async function commandInspect(state: State, ...args: string[]) {
  if (args.length === 0) {
    console.log("Command should have a pokemon name to inspect");
    return;
  }

  const pokemon = state.pokedex[args[0]]
  if (!pokemon) {
    console.log("you have not caught that pokemon");
    return;
  }

  console.log(`Name: ${pokemon.name}`);
  console.log(`Height: ${pokemon.height}`);
  console.log(`Weight: ${pokemon.weight}`);
  console.log("Stats:");
  pokemon.stats.map((stat) => {
    console.log(`  -${stat.stat.name}: ${stat.base_stat}`)
  })
  console.log("Types:");
  pokemon.types.map((type) => {
    console.log(`  -${type.type.name}`)
  })

  
  return;
}