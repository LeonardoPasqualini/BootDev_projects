import { startREPL } from "./repl.js";
import { initState, State } from "./state.js";


function main() {
  const state: State = initState();
  startREPL(state);
}

main();