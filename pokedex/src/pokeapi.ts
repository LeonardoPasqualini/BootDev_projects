import { Cache } from "./pokecache.js"

export class PokeAPI {
  private static readonly baseURL = "https://pokeapi.co/api/v2";

  cache = new Cache(5000);

  constructor() {
    this.cache.stopReapLoop();
  }

  async fetchLocations(pageURL?: string): Promise<ShallowLocations> {

    const locationAreaURL = pageURL ?? `${PokeAPI.baseURL}/location-area`;
    const cachedLocation = this.cache.get(locationAreaURL)
    // lookup for cached url
    if (cachedLocation) {
      return cachedLocation as ShallowLocations
    }

    let locations: ShallowLocations;
    try {
      const response = await fetch(locationAreaURL, {
        method: "GET",
        mode: "cors"
      });
      if (response.ok) {
        locations = await response.json()
        this.cache.add(locationAreaURL, locations);
      }else {
        throw new Error(`Fetching locattions Response failed: ${response.status} - ${response.statusText}`);
      }

    } catch (err) {
      console.error(err);
      throw new Error(`Fetching locattions failed: ${(err as Error).message}`);
    }

    return locations;
  }

  async fetchLocation(locationName: string): Promise<LocationArea> {
    const locationNameURL = `${PokeAPI.baseURL}/location-area/${locationName}`;

    // lookup for cached url
    if (this.cache.get(locationNameURL)) {
      return this.cache.get(locationNameURL) as LocationArea
    }

    let locationsArea;
    try {
      const response = await fetch(locationNameURL, {
        method: "GET",
        mode: "cors"
      });
      if (response.ok) {
        locationsArea = await response.json()
        this.cache.add(locationNameURL, locationsArea);
      }else {
        throw new Error(`Fetching location Response failed: ${response.status} - ${response.statusText}`);
      }
    } catch (err) {
      throw new Error((err as Error).message);
    }

    return locationsArea;

  }
}

export type ShallowLocations = {
  results: LocationResult[],
  next: string | null,
  previous: string | null,
};

export type LocationResult = {
  name: string,
  url: string,
};

export type LocationArea = {
  pokemon_encounters: Encounter[]
}

export type Encounter = {
  pokemon: Pokemon
}

export type Pokemon = {
  name: string
  url: string
}