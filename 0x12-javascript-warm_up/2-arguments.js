#!/usr/bin/node

const args = process.argv.slice(2);
const noArgs = "No argument";
const oneOrMoreArgs = "Argument found";

if (args.length === 0){
	console.log(noArgs);
}
else if (args.length === 1){
	console.log(oneOrMoreArgs);
}
else {
	console.log(oneOrMoreArgs);
}
