import React, { Component } from 'react';
import Square from './components/Square';
import Layout from './components/Layout';
import Row from './components/Row';

class App extends Component {
  render() {
    return (
      <div className="App" style={{height: '100vh', width: '100vw'}}>
					<Square></Square>
      </div>
    );
  }
}

export default App;