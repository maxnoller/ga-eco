import React from "react";
import ReactDOM from "react-dom";
import Environment from "./environment";

const App = () => (
  <React.Fragment>
    <Environment />
  </React.Fragment>
);

const wrapper = document.getElementById("app");
wrapper ? ReactDOM.render(<App />, wrapper) : null;
