import React, { Component } from "react";
import { Table } from "reactstrap";
import SeeDetail from "./SeeDetail";


class StudentList extends Component {
  render() {
    const students = this.props.students;
    return (
      <Table striped bordered hover>
        <thead>
          <tr>
            <th>Company</th>
            <th>Salary</th>
            <th>City</th>
            <th>Year</th>
            <th>Date Posted</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          {!students || students.length <= 0 ? (
            <tr>
              <td colSpan="6" align="center">
                <b>No data Available</b>
              </td>
            </tr>
          ) : (
            students.map(student => (
              <tr key={student.pk}>
                <td>{student.company}</td>
                <td>${student.salary}</td>
                <td>{student.city}</td>
                <td>{student.grade_year}</td>
                <td>{student.post_date}</td>
                <td align="center">
                  <SeeDetail
                    student={student}
                    resetState={this.props.resetState}
                  />
                </td>
              </tr>
            ))
          )}
        </tbody>
      </Table>
    );
  }
}

export default StudentList;
