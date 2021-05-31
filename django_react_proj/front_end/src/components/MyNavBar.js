import Navbar from 'react-bootstrap/Navbar';
import Nav from 'react-bootstrap/Nav';
import React, { Component } from "react";



class MyNavBar extends Component{
    render(){
        return(
            <Navbar bg="primary" variant="dark">
                <Navbar.Brand href="/">Tech Intern Info</Navbar.Brand>
                <Nav className="mr-auto">
                  <Nav.Link href="/">Home</Nav.Link>
                  <Nav.Link href="/search">Search</Nav.Link>
                  <Nav.Link href="/cpdata">Company</Nav.Link>
                </Nav>
              </Navbar>
        );
    }
}
export default MyNavBar;
