import React from 'react';

export default class Square extends React.Component {

  constructor(props) {
    super(props);

    this.colors = ['red', 'green', 'blue', 'pink', 'purple'];

    this.state = {
      colorIndex: 0
    };
  }

  myOnClick() {
    let newIndex = this.state.colorIndex + 1;
    if(newIndex > this.colors.length) {
      newIndex = 0;
    }

    this.setState({
      colorIndex: newIndex
    });
  }

  render() {
    return (
      <div className='square'
        style={{
          justifyContent: 'center',
          height: '95vh',
          width: '95vw',
          backgroundColor: '#8BC2FF',
          borderRadius: '95px',
          border: '1px solid black'
        }}
        onClick={this.myOnClick.bind(this)}
      >
       {this.text}
      </div>
    )
  }
}