// Write a javascript function that simulates asynchronous behaviour using setTimeout().The function should take a callback
// as an argument and execute it after a specified delay.
function simulate(callback,delay){
    if(typeof callback !== 'function'){
        throw new Error('The first argument must be a function.');
    }
    if(typeof delay !== 'number' || delay < 0){
        throw new Error('The second argument represents DELAY in milliseconds.');
    }
    setTimeout(() => {
        callback();
    },delay);
}
simulate(() => {
    console.log('Mithil 2310997173');
},4000);

// setTimeout(()=>{
//     console.log("Mithil 2310997173");
// },2000);