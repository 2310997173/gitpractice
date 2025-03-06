console.log("Mithil");
console.log("2310997173");
const student = `{
    "Name" : "Virat",
    "age" : 37,
    "email" : "Virat_kholi@gmail.com",
    "course" : ["FED","Python","Testing"]
}`;
console.log("Original data");
console.log(student);
console.log(typeof(student));
JSON.parse(student);