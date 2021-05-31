import React, { Component, Fragment } from "react";
import Home from "./components/Home";
import MyNavBar from "./components/MyNavBar";
import SearchForm from "./components/SearchForm";
import CompanyDataList from "./components/CompanyDataList";
import {BrowserRouter as Router,Route, Redirect,Switch} from 'react-router-dom';

class App extends Component {
  render() {
    return (
      <Fragment>
      <Router>
            <div>
              <MyNavBar />
              <Switch>
                 <Route path="/cpdata" component = {CompanyDataList} />
                 <Route path="/search" component = {SearchForm} />
                 <Route path="/" component = {Home} />
              </Switch>
            </div>
      </Router>

      </Fragment>
    );
  }
}

export default App;
