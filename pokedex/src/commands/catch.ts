import { Encounter, Pokemon } from "../pokeapi.js";
import { State } from "../state.js";


export async function commandCatch(state: State, ...args: string[]) {
  if (args.length === 0) {
    console.log("Command should have a pokemon name to catch");
    return;
  }
  const pokeAPI = state.pokeAPI;
  const pokemonName = args[0];
  try {
    const response = await pokeAPI.fetchPokemon(pokemonName);

    console.log(`Throwing a Pokeball at ${pokemonName}...`)

    const chance = (Math.random() / response.base_experience) * 650
    if (chance < 1) {
      console.log(`${pokemonName} was caught!`);
      state.pokedex[pokemonName] = response as Pokemon;
    } else {
      console.log(`${pokemonName} escaped!`)
    }

  } catch (err) {
    console.log(`Fetching location failed: ${(err as Error).message}`);
  }

  return;
}