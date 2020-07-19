import React from 'react';
import Button from 'react-bootstrap/lib/Button';
import ButtonGroup from "react-bootstrap/lib/ButtonGroup";
import Row from 'react-bootstrap/lib/Row';
import Col from 'react-bootstrap/lib/Col';

class ControlPanel extends React.Component {
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
      <Row style={{paddingLeft: 15}}>
      <ButtonGroup style={{width: "100%"}}>
          <Col style={{padding: 0}}><Button style={{borderRadius: 0, border: "1px solid black"}} block>Environment</Button></Col>
          <Col style={{padding: 0}}><Button style={{borderRadius: 0, border: "1px solid black"}} block>Vehicles</Button></Col>
          <Col style={{padding: 0}}><Button style={{borderRadius: 0, border: "1px solid black"}} block>Statistics</Button></Col>
      </ButtonGroup>
      </Row>
  );
  }
}

export default ControlPanel;
