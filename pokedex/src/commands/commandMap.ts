import { State } from "../state.js";


export async function commandMap(state: State) {
  const pokeAPI = state.pokeAPI;
  const response = await pokeAPI.fetchLocations(state.nexLocationURL);

  state.nexLocationURL = response.next;
  state.prevLocationURL = response.previous;

  response.results.map((location) => {
    console.log(location.name)
  });

  return;
}

export async function commandMapB(state: State) {
  const pokeAPI = state.pokeAPI;
  if (!state.prevLocationURL) {
    console.log("you're on the first page");
    return;
  }
  const response = await pokeAPI.fetchLocations(state.prevLocationURL);

  state.nexLocationURL = response.next;
  state.prevLocationURL = response.previous;

  response.results.map((location) => {
    console.log(location.name)
  });

  return;
}