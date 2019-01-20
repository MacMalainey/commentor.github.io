import React from 'react';

export default class xLabels extends React.Component {

  constructor(props) {
    super(props);

    this.colors = ['red', 'green', 'blue', 'pink', 'purple'];

    this.state = {
      colorIndex: 0
    };
  }

  
  render() {
    return (
      <div className='square'
        style={{
          justifyContent: 'center',
          height: '95vh',
          width: '80vw',
          alignSelf: 'center',
          backgroundColor: '#8BC2FF'
        }}
      >
      
      <BarGraph></BarGraph>
      </div>
    )
  }
}