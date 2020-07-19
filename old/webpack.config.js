const path = require('path');
module.exports = {
  module: {
    rules: [
      {
        test : /\.js$/,
        exclude: [/node_modules/, path.resolve(__dirname, "src/components/sketches/")],
        loader: 'babel-loader'
      }
    ]
  }
};
