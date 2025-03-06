// Demonstrate the concept of closure by calling the inner function & accessing the outer variables.
function outFunc(){
    let outVar = "Outer Variable";
    function inFunc(){
        console.log(outVar);
    }
    return inFunc;
}
const closure = outFunc();
closure();