import React, { useState } from 'react';

function App() {
  const [currentFact, setCurrentFact] = useState("Loading...")

  function handleClick(){
    fetch('/facts')
      .then(response => response.json())
      .then(data =>{ setCurrentFact(data.fact); console.log(data)});
  }

  return (
    <div className="App">
      <p>The current fact is: {currentFact}</p>  
      <button onClick={handleClick}>Click Me!</button>
    </div>
  );
}

export default App;
