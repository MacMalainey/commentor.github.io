import React from 'react';

export default class BarGraph extends React.Component {

  constructor(props) {
    super(props);

    this.colors = ['red', 'green', 'blue', 'pink', 'purple'];
    this.text = ['red', 'green', 'blue', 'pink', 'purple'];
    this.state = {
      colorIndex: 0
    };
  }


  render() {
    return (
      <div className='square'
        style={{
          justifyContent: 'center',
          height: '100%',
          width: '20%',
          textAlign: 'center',
          backgroundColor: '#f2cfae',
        }}
      >
      {this.text[0]}

      </div>
    )
      }
}