import React from "react"

function App(){
  const student ={
    nm : "Mithil",
    rno : "7173",
    sub : "Front End Development"
  };
  const msg = `My Name = ${student.nm} & Roll Number = ${student.rno}.
  Learning ${student.sub}`;
  return (
    <div style = {{ fontFamily : "Times New Roman",
      textAlign : "center" , marginTop : "50px"}}>
      <h1>Working with tempate literals in React.js</h1>
      <h2>{msg}</h2>
    </div>  
  );
}
export default App;