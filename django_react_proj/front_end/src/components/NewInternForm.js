import React from "react";
import { Button} from "reactstrap";

import axios from "axios";
import {Col, Form, } from 'react-bootstrap';
import { List_URL } from "../constants";

class NewStudentForm extends React.Component {
  state = {
    company: "",
    salary:  0.0,
    city: "",
    state: "",
    grade_year: "Junior",
    job_role: "Back End SWE",
    prev_exp_num: "0",
    prev_exp_det: "",
    university: "",
    gpa: null,
    jobs_applied: "1-10",
    housing: "Corporate Housing",
    housing_amount: null,
    comment: "",
    checked: "first",
  };

  componentDidMount() {
  }

  onChange = e => {
    console.log("e.target.value =", e.target.value);
    this.setState({ [e.target.name]: e.target.value });
  };

  onChangeNum = e => {
    var integer = parseInt(e.target.value, 10);
    console.log("e.target.value =", e.target.value);
    this.setState({ [e.target.name]:  integer});
  };

  onChangeFloat = e => {
    var float;
    float = parseFloat(e.target.value)
    console.log("e.target.value =", e.target.value);
    this.setState({ [e.target.name]:  float});
  };

    createStudent = e => {
        e.preventDefault();
        console.log(this.state);
        axios.post(List_URL, this.state).then((response) => {
          this.props.resetState();
          this.props.toggle();
          console.log(response)
        });
    };


  sorter = e => {
    this.setState({checked:e.target.id});
  }

  snip_amount = () =>{
    if(this.state.housing === "Housing Stipend"){
      return(
        <Form.Group as={Col} md="3" className="ml-1" as={Col} controlId="formGridZip">
        <Form.Control onChange={this.onChange} value={this.state.housing_amount} type="number" name="housing_amount" type="number" placeholder="$ Housing Snippend"/>
        </Form.Group>
      );
    }
  }


  render() {
    return (
      <Form onSubmit={this.createStudent}>
        <Form.Row>
          <Form.Group as={Col} md="7">
            <Form.Label>Company</Form.Label>
            <Form.Control onChange={this.onChange} value= {this.state.company} type="text" name="company" placeholder="Compnany Name" required />
          </Form.Group>

          <Form.Group as={Col} md="3" className="ml-3" >
            <Form.Label>Salary</Form.Label>
            <Form.Control onChange={this.onChangeNum}  type="number" step="0.1" name="salary" placeholder="Salary" required />
          </Form.Group>
        </Form.Row>

        <Form.Row>
          <Form.Group as={Col} md="7" >
            <Form.Label>City</Form.Label>
            <Form.Control onChange={this.onChange} value={this.state.city} type="text" name="city" placeholder="Office City" required />
          </Form.Group>

          <Form.Group as={Col} md="3" className="ml-3">
            <Form.Label>State ID</Form.Label>
            <Form.Control onChange={this.onChange} value={this.state.state} type="text" name="state" placeholder="CA, NY, etc..." required />
          </Form.Group>
      </Form.Row>

      <Form.Row>
          <Form.Group as={Col} md="6" >
            <Form.Label>University</Form.Label>
            <Form.Control onChange={this.onChange} value={this.state.university} type="text" name="university" placeholder="University Name (optional)"  />
          </Form.Group>

          <Form.Group controlId="exampleForm.SelectCustom">
            <Form.Label>Year</Form.Label>
            <Form.Control onChange={this.onChange} value={this.state.grade_year} name="grade_year" as="select" custom>
              <option value="Freshman">Freshman</option>
              <option value="Sophmore">Sophmore</option>
              <option value="Junior">Junior</option>
              <option value="Senior">Senior</option>
            </Form.Control>
          </Form.Group>

          <Form.Group as={Col} md="2" >
            <Form.Label>GPA</Form.Label>
            <Form.Control onChange={this.onChangeFloat} value={this.state.gpa} type="number" name="gpa" placeholder="optional" />
          </Form.Group>
      </Form.Row>

      <Form.Row>
          <Form.Group as={Col} md="2" controlId="exampleForm.SelectCustom">
            <Form.Label>Jop Type</Form.Label>
            <Form.Control onChange={this.onChange} value={this.state.job_role} type="text" name="job_role" as="select" custom>
              <option value="Back End">Back End</option>
              <option value="Front End">Front End</option>
              <option value="Full Stack">Full Stack</option>
              <option value="UX Design">UX Design</option>
              <option value="Mobile Development">Mobile Development</option>
              <option value="Embeded Systems">Embeded Systems</option>
              <option value="AI / Machine Learning">AI / Machine Learning</option>
              <option value="Data Science">Data Science</option>
              <option value="Product Design">Product Design</option>
            </Form.Control>
          </Form.Group>

          <Form.Group as={Col} md="4" className="ml-2" controlId="exampleForm.SelectCustom">
            <Form.Label>Number of Previous Internships</Form.Label>
            <Form.Control onChange={this.onChange} value={this.state.prev_exp_num} type="number" name="prev_exp_num" as="select" custom>
              <option value="0">0</option>
              <option value="1">1</option>
              <option value="2">2</option>
              <option value="3">3</option>
              <option value="4">4</option>
              <option value="5">5</option>
              <option value="5+">5+</option>
            </Form.Control>
          </Form.Group>

          <Form.Group as={Col} md="4" className="ml-2" controlId="exampleForm.SelectCustom1">
            <Form.Label>Number of Jobs Applied This Year</Form.Label>
            <Form.Control onChange={this.onChange} value={this.state.jobs_applied} name="jobs_applied" as="select" custom>
              <option value="1-10">1-10</option>
              <option value="11-20">11-20</option>
              <option value="21-30">21-30</option>
              <option value="31-40">31-40</option>
              <option value="41-50">41-50</option>
              <option value="51-60">51-60</option>
              <option value="61-70">61-70</option>
              <option value="71-80">71-80</option>
              <option value="80+">80+</option>
            </Form.Control>
          </Form.Group>
      </Form.Row>

      <Form.Row>
        <Form.Group controlId="formBasicCheckbox">
            <Form.Check onChange={ e => {this.onChange(e); this.sorter(e)}} id="first" checked={this.state.checked==='first'}  value="Corporate Housing" name="housing" className="mt-2" type="checkbox" label="Corporate Housing" />
        </Form.Group>
        <Form.Group className="ml-2 mt-2" controlId="formBasicCheckbox">
            <Form.Check onChange={ e => {this.onChange(e); this.sorter(e)}} id="second" checked={this.state.checked==='second'} value="Housing Stipend" name="housing" type="checkbox" label="Housing Stipend" />
        </Form.Group>
        <Form.Group className="ml-2 mt-2" controlId="formBasicCheckbox">
            <Form.Check onChange={ e => {this.onChange(e); this.sorter(e)}} id="third" checked={this.state.checked==='third'} value="No Housing Support" name="housing" type="checkbox" label="No Housing Support" />
        </Form.Group>
        {this.snip_amount()}
      </Form.Row>

      <Form.Row>
        <Form.Group controlId="exampleForm.ControlTextarea1">
          <Form.Label>Any Other Info</Form.Label>
          <Form.Control onChange={this.onChange} value={this.state.comment} name="comment" as="textarea" rows="3" placeholder=""/>
        </Form.Group>
      </Form.Row>


        <Button>Send</Button>
      </Form>
    );
  }
}

export default NewStudentForm;
