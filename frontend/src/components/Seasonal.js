import React, { Component } from "react";
import { render } from "react-dom";

class Seasonal extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [],
      loaded: false,
      placeholder: "Loading"
    };
  }

  componentDidMount() {
    fetch("api/inseason")
      .then(response => {
        if (response.status > 400) {
          return this.setState(() => {
            return { placeholder: "Something went wrong!" };
          });
        }
        return response.json();
      })
      .then(data => {
        this.setState(() => {
          return {
            data,
            loaded: true
          };
        });
      });
  }

  render() {
    return (
      <ul>
        {this.state.data.map(produce => {
          return (
            <li key={produce.name}>
              {produce.name} - {produce.sub_names} - {produce.usda_url} - {produce.category}
            </li>
          );
        })}
      </ul>
    );
  }
}

export default Seasonal;

const container = document.getElementById("app");
render(<Seasonal />, container);