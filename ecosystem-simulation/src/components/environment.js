import React from 'react';
import p5 from "p5";
import environmentSketch from "./sketches/environmentSketch";
import testSketch from "./sketches/testSketch";


class Environment extends React.Component {
  constructor(props) {
    super(props);
    this.state = { width: 0, height: 0};
    this.updateWindowDimensions = this.updateWindowDimensions.bind(this);
  }

  componentDidMount() {
    this.canvas = new p5(testSketch, this.wrapper);
    if( this.canvas.myCustomRedrawAccordingToNewPropsHandler ) {
      this.canvas.myCustomRedrawAccordingToNewPropsHandler(this.props);
    }

    this.updateWindowDimensions();
    window.addEventListener('resize', this.updateWindowDimensions);
  }

  componentWillReceiveProps(newprops) {
    if( this.canvas.myCustomRedrawAccordingToNewPropsHandler ) {
      this.canvas.myCustomRedrawAccordingToNewPropsHandler(newprops);
    }
  }

  componentWillUnmount() {
    window.removeEventListener('resize', this.updateWindowDimensions);
  }

  updateWindowDimensions() {
    this.setState({ width: this.refs.env.parentNode.getBoundingClientRect().width, height: this.refs.env.parentNode.getBoundingClientRect().height});
  }

  render() {
    return (
    <div ref="env"><div ref={wrapper => this.wrapper = wrapper}></div></div>
  );
  }
}

export default Environment;
