// WAP to check whether the number is positive ,negative or 0 and print the resut accordingly
const prompt = require("prompt-sync")();
let n = 5;
if(n==0){
    console.log("Zero");
}
else if(n>0){
    console.log("Positive");
}
else console.log("Negative");

console.log("By Dynamic Way")
    n = parseInt(prompt("Enter the number: "));
    if(n==0){
        console.log("zero");
    }
    else if(n>0){
        console.log("Positive");
    }
    else{
        console.log("Negative");
    }