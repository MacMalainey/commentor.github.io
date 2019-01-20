import React from 'react';
import BarGraph from './BarGraph';
import yAxis from './yAxis';
import Bars from './Bars';
import Windows from './Window';
import xAxis from './xAxis';
import xLabels from './xLabels';


export default class Square extends React.Component {

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
      <Windows></Windows>

      </div>
    )
  }
}