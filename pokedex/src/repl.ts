// import { commandExit } from "./commands/exit.js";
// import { commandHelp } from "./commands/help.js";
import { CLICommand, State } from "./state.js";
// npm run dev | tee repl.log

// export function getCommands(): Record<string, CLICommand> {
//   return {
//     exit: {
//       name: "exit",
//       description: "Exit the Pokedex",
//       callback: commandExit,
//     },
//     help: {
//       name: "help",
//       description: "Displays available commands",
//       callback: commandHelp,
//     },
//     // can add more commands here
//   };
// }

export function cleanInput(input: string): string[] {
  const splitArray = input.trim().split(" ");
  let cleanArr = [];
  for (let word of splitArray) {
    if (!word.length) {
      continue;
    }
    cleanArr.push(word.toLowerCase())
  }
  return cleanArr;
}

export async function startREPL(state: State) {
  const rl = state.rl

  rl.prompt()
  rl.on("line", async (line) => {
    const inputClean = cleanInput(line);
    const commands = state.commands;
    // clean output
    if (inputClean.length == 0) {
      rl.prompt()
      return;
    }

    try {
      // lookup the command
      const command = commands[inputClean[0]];
console.log(command)
      // if command doesn't exist log unknow command
      // else call the command
      if (!command) {
        console.log("Unknown command");
      } else {
        const call = command.callback(state);
        await call;
      }
    } catch (err) {
      console.log("Error", err);
    }
    // gives back the prompt to user
    rl.prompt();
  });
}

export { CLICommand };
