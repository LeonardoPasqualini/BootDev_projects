import { startREPL } from "./repl.js";
import { initState, State } from "./state.js";


async function main() {
  try {
    const state: State = initState();
    await startREPL(state);
  } catch (error) {
    console.error(error);
  }
  
}

await main();