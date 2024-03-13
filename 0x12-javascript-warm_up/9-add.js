#!/usr/bin/node

function add (a, b) {
  let arg = process.argv;
  a = parseInt(process.argv[2]);
  b = parseInt(process.argv[3]);

  if (arg.length === 4) {
    return (a + b);
  } else {
    return ('NaN');
  }
}
console.log(add());
