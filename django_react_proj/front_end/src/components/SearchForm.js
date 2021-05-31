import React, {Component} from 'react';
import {Col, Form, Button} from 'react-bootstrap';
import Pagination from 'react-bootstrap/Pagination'
import axios from "axios";
import StudentList from "./InternList";
import { Search_URL } from "../constants";

class SearchForm extends Component{

    state = {
        company : "",
        city: "",
        max_salary: 100000000000,
        min_salary: 0,
        students : [],
        next: "",
        prev: "",
        limit: 20,
        resultNum: 0
    }

    onChange = e => {
        console.log("e.target.value =", e.target.value);
        this.setState({ [e.target.name]: e.target.value });
     };

   onChangeNum = e => {
      var integer = 0;
      if( e.target.value == ""){
        if(e.target.name == "min_salary"){ integer = 0;}
        if(e.target.name == "max_salary"){ integer = 10000;}
      }
      else{
        var integer = parseInt(e.target.value, 10);
      }
      console.log("e.target.value =", e.target.value);
      console.log("integer =", integer);
      this.setState({ [e.target.name]:  integer});
    };

    onChangeLimit = e => {
       console.log("e.target.value =", e.target.value);
       this.setState({limit : e.target.value});
     };

     getNext = () => {
           axios.get(this.state.next).then(res => this.setState({ students: res.data.results, next: res.data.next, prev: res.data.previous})).then(console.log(this.state));
         };

    getPrev = () => {
        axios.get(this.state.prev).then(res => this.setState({ students: res.data.results, next: res.data.next, prev: res.data.previous})).then(console.log(this.state));
      };

    searchData = () => {
        //e.preventDefault();
        console.log(this.state);
        axios.get(Search_URL +"/?limit=" + this.state.limit + "&salary_min="+this.state.min_salary+"&salary_max="+this.state.max_salary+"&order_by=salary&company=" + this.state.company +"&city=" + this.state.city).
        then( res => {
            this.setState({ students: res.data.results, next: res.data.next, prev: res.data.previous, resultNum : res.data.count});
            console.log(res.data);
        });

    };


    render(){
        return(
            <div className="container">

               <Form>
                 <Form.Row >
                     <Form.Group as={Col} md="3" >
                        <Form.Label>Company</Form.Label>
                        <Form.Control onChange={this.onChange}  type="text" name="company" placeholder="Any company if blank" />
                    </Form.Group>

                    <Form.Group as={Col} md="3" >
                        <Form.Label>City</Form.Label>
                        <Form.Control onChange={this.onChange}  type="text" name="city" placeholder="Any city if blank"/>
                    </Form.Group>
                 </Form.Row>


                <Form.Row>
                  <Form.Group as={Col} md="3">
                    <Form.Label>Salary-Min</Form.Label>
                    <Form.Control onChange={this.onChangeNum}  type="number" step="0.1" name="min_salary" placeholder="$ per hour (No min if blank)" required />
                  </Form.Group>

                  <Form.Group as={Col} md="3">
                    <Form.Label>Salary-Max</Form.Label>
                    <Form.Control onChange={this.onChangeNum}  type="number" step="0.1" name="max_salary" placeholder="$ per hour (No max if blank)" required />
                  </Form.Group>
                </Form.Row>

                <Button className="mb-3" onClick={this.searchData} variant="primary">Search</Button>
               </Form>

            <Form>
              <Form.Group as={Col} md="2" style={{paddingLeft: "0rem"}} >
                <Form.Label style={{marginBottom: "0rem"}}>Per Page Results</Form.Label>
                <Form.Control onChange={this.onChangeLimit} as="select">
                  <option>20</option>
                  <option>50</option>
                  <option>100</option>
                </Form.Control>
              </Form.Group>
            </Form>

            <p>
                {this.state.resultNum} matches found
            </p>

           <StudentList
             students={this.state.students}
           />

           <div className="center">
               <Pagination>
                 <Pagination.First />
                 <Pagination.Prev onClick={this.getPrev} />
                 <Pagination.Next onClick={this.getNext} />
                 <Pagination.Last />
               </Pagination>
           </div>
        </div>
        );
    }
  }

export default SearchForm;
