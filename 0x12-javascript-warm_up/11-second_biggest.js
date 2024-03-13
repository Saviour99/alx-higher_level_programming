#!/usr/bin/node

if (process.argv.slice(2).length > 0) {
  const sortArgs = process.argv.slice(2).map(Number).sort((a, b) => a - b);
  console.log(sortArgs[sortArgs.length - 2]);
} else {
  console.log(0);
}
