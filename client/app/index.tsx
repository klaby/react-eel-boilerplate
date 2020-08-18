import React, { useEffect } from 'react'

const App: React.FC = () => {
  useEffect(() => {
    window.eel.hello()
  }, [])

  return <h1>React Eel Boilerplate</h1>
}

export default App
