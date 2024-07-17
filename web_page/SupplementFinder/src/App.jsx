import { useState } from 'react';
import './CSS/App.css';
import Navbar from './navbar';

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <Navbar/>
      <h1>Supplement Finder</h1>
    </>
  )
}

export default App
