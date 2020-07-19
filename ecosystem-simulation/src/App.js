import React, { Component } from 'react';
import './App.css';
import Environment from "./components/environment";
import ControlPanel from "./components/ControlPanel";
import Container from 'react-bootstrap/lib/Container';
import Row from 'react-bootstrap/lib/Row';
import Col from 'react-bootstrap/lib/Col';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = { width: 0, height: 0 };
    this.updateWindowDimensions = this.updateWindowDimensions.bind(this);
  }

  componentDidMount() {
    this.updateWindowDimensions();
    window.addEventListener('resize', this.updateWindowDimensions);
  }

  componentWillUnmount() {
    window.removeEventListener('resize', this.updateWindowDimensions);
  }

  updateWindowDimensions() {
    this.setState({ width: window.innerWidth, height: window.innerHeight });
  }
  render() {
    return (
      <Container fluid>
        <Row>
          <Col lg={6} id="envCol" style={{padding: 0}}><Environment /></Col>
          <Col lg={6} style={{padding: 0}}><ControlPanel /></Col>
        </Row>
      </Container>
    );
  }
}

export default App;
