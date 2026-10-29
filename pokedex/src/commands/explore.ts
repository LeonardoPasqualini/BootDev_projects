import { Encounter } from "../pokeapi.js";
import { State } from "../state.js";


export async function commandExplore(state: State, ...args: string[]) {
  if (args.length === 0) {
    console.log("Command should have the location name or id to explore");
    return;
  }
  const pokeAPI = state.pokeAPI;
  console.log(`Exploring ${args[0]}...`)
  try {
    const response = await pokeAPI.fetchLocation(args[0]);
    console.log("Found Pokemon:")
    response.pokemon_encounters.map((encounter: Encounter) => {
      console.log("- ", encounter.pokemon.name)
    });
  } catch (err) {
    console.log(`Fetching location failed: ${(err as Error).message}`);
  }

  return;
}