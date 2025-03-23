console.log("Mithil");
console.log("2310997173");
let a = 7;
{
    let b = 9;
    console.log("Variable b is local"+ b);
}
console.log("Variable a is global"+ a);

function demo()
{
    let c = 27;
    console.log("Variable a as global"+ a);
    console.log("Varibale c as function"+ c);
}
demo();
console.log("Variable a as global"+ a);