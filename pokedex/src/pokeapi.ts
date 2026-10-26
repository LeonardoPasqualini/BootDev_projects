export class PokeAPI {
  private static readonly baseURL = "https://pokeapi.co/api/v2";

  constructor() { }

  async fetchLocations(pageURL?: string): Promise<ShallowLocations> {
  
    const locationAreaURL = pageURL ?? `${PokeAPI.baseURL}/location-area`;
    
    let locations;
    try {
      const response = await fetch(locationAreaURL, {
        method: "GET",
        mode: "cors"
      });
      locations = await response.json()
      // locations = jsonRes.results
    } catch (err) {
      console.log(err instanceof TypeError);
    }

    return locations;
  }

  // async fetchLocation(locationName: string): Promise<Location> {


  // }
}

export type ShallowLocations = {
  results: Result[],
  next: string,
  previous: string,
};

export interface Result {
  name: string
  url: string
}

export type Location = {

};