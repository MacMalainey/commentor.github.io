import React from 'react';

export default class Row extends React.Component {

	constructor(props) {
		super(props);
	}

	renderChildren() {
		let changed;
		changed = this.props.children.map( (child, index) => {
			return (
				<div style={{float: 'left', paddingRight: '10px', 
				justifyContent: 'center'}}>
					{child}
				</div>
			)
		});
		return changed;
	}

	render() {
		return (
			<div className='row' style={{
				display: 'table',
				justifyContent: 'center',
				}}>
				{this.renderChildren()}
			</div>
		)
	}
}