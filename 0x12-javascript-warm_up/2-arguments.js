#!/usr/bin/node

const args = process.argv;
const noArgs = 'No argument';
const oneOrMoreArgs = 'Argument found';

if (args.length === 2) {
  console.log(noArgs);
} else if (args.length === 3) {
  console.log(oneOrMoreArgs);
} else {
  console.log(oneOrMoreArgs);
}
