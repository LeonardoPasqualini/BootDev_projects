import { Cache } from "./pokecache.js"

export class PokeAPI {
  private static readonly baseURL = "https://pokeapi.co/api/v2";

  cache = new Cache(5000);

  constructor() {
    this.cache.stopReapLoop();
  }

  async fetchLocations(pageURL?: string): Promise<ShallowLocations> {

    const locationAreaURL = pageURL ?? `${PokeAPI.baseURL}/location-area`;

    // lookup for cached url
    if (this.cache.get(locationAreaURL)) {
      return this.cache.get(locationAreaURL) as ShallowLocations
    }

    let locations;
    try {
      const response = await fetch(locationAreaURL, {
        method: "GET",
        mode: "cors"
      });
      locations = await response.json()
      this.cache.add(locationAreaURL, locations);
    } catch (err) {
      console.log(err instanceof TypeError);
    }

    return locations;
  }

  // async fetchLocation(locationName: string): Promise<Location> {


  // }
}

export type ShallowLocations = {
  locations: Location[],
  next: string,
  previous: string,
};

export interface Location {
  name: string
  url: string
};