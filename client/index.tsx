import React from 'react'
import { render } from 'react-dom'

import App from './app'

window.eel.set_host('ws://localhost:8080')

render(<App />, document.getElementById('root'))
