console.log("Mithil");
console.log("2310997173");
const prompt = require("prompt-sync")();
const add = function(a,b){
    let c = a + b;
    return c;
}
let x = parseInt(prompt("Enter first number: "));
let y = parseInt(prompt("Enter second number: "));
let result = add(x,y);
console.log("Sum of "+x+" + "+y+ " = " + result);