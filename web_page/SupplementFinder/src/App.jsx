import { useState } from 'react';
import './CSS/App.css';
import Navbar from './navbar';
import Chatbot from './chatbot';

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <Navbar/>
      <Chatbot/>
    </>
  )
}

export default App
