// Write a javascript function that attempts to parse a JSON string. Use a try-catch block to handle any errors that
// may occur during parsing. If successfull, log the parsed data; otherwise, log an error message.
function JSONParse(jsonString){
    try{
        const parsedData = JSON.parse(jsonString);
        console.log("Parsed Data: ",parsedData);
    }catch(error){
        console.error("Error parsing JSON: ",error.message);
    }
}
JSONParse('{"name": "Mithil","rno": 7173}');
JSONParse('Invalid JSON String');