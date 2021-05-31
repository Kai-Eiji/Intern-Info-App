import React, {Component} from 'react';
import {Col, Form, Button, Badge, Table} from 'react-bootstrap';
import Card from 'react-bootstrap/Card'
import axios from "axios";
import { Company_Info_URL } from "../constants";
import CanvasJSReact from './canvasjs.react';
var CanvasJS = CanvasJSReact.CanvasJS;
var CanvasJSChart = CanvasJSReact.CanvasJSChart;

class CompanyData extends Component{

    state = {
        company : "N/A",
        final_company_name : "N/A",
        total_ave : null,
        total_max : null,
        total_min : null,
        total_count : null,
        fre_ave : null,
        fre_max : null,
        fre_min : null,
        fre_count : null,
        sop_ave : null,
        sop_max : null,
        sop_min : null,
        sop_count : null,
        jun_ave : null,
        jun_max : null,
        jun_min : null,
        jun_count : null,
        sen_ave : null,
        sen_max : null,
        sen_min : null,
        sen_count : null,
        locations : [],
        deleted : false,
    }

    onChange = e => {
            console.log("e.target.value =", e.target.value);
            this.setState({ [e.target.name]: e.target.value });
    };

    round = val => {
        if(val === null){
            return val
        }
        else{
            return val.toFixed(2);
        }
    }

    searchData = () => {
        //e.preventDefault();
        this.setState({final_company_name : this.state.company});
        axios.get(Company_Info_URL +"/?company=" + this.state.company).
        then( res => {
            this.setState({ locations : res.data.cities, total_ave : this.round(res.data.total.avg.salary__avg), total_max : res.data.total.max.salary__max, total_min : res.data.total.min.salary__min, total_count : res.data.total.count,
                            fre_ave : this.round(res.data.freshmen.avg.salary__avg), fre_max : res.data.freshmen.max.salary__max, fre_min : res.data.freshmen.min.salary__min, fre_count : res.data.freshmen.count,
                            sop_ave : this.round(res.data.sophmore.avg.salary__avg), sop_max : res.data.sophmore.max.salary__max, sop_min : res.data.sophmore.min.salary__min, sop_count : res.data.sophmore.count,
                            jun_ave : this.round(res.data.junior.avg.salary__avg), jun_max : res.data.junior.max.salary__max, jun_min : res.data.junior.min.salary__min, jun_count : res.data.junior.count,
                            sen_ave : this.round(res.data.senior.avg.salary__avg), sen_max : res.data.senior.max.salary__max, sen_min : res.data.senior.min.salary__min, sen_count : res.data.senior.count,
                            locations : res.data.cities,
            });
        });

    };

    deleteCompanyData = () =>{
        this.setState({deleted : true});
    }


    render() {
    		const options = {
    			animationEnabled: true,
    			title:{
    				text: "Salary Range of " + this.state.final_company_name,
    				fontFamily: "helvetica"
    			},
    			axisY: {
    				title: "",
    				prefix: "$",
    				lineThickness: 1
    			},
    			data: [{
    				type: "rangeBar",
    				indexLabel: "${y[#index]}",
    				dataPoints: [
    					{ label: "Senior", y: [this.state.sen_min, this.state.sen_max] },
    					{ label: "Junior", y: [this.state.jun_min, this.state.jun_max] },
    					{ label: "Sophomore", y: [this.state.sop_min, this.state.sop_max] },
    					{ label: "Freshmen", y: [this.state.fre_min, this.state.fre_max] },
    					{ label: "Total", y: [this.state.total_min, this.state.total_max] }
    				]
    			}]
    		}

    		if(this.state.deleted){
    		    return(<p></p>);

    		}
    		return (

    		<Card border="dark" className="m-5">
                <Card.Body>

                    <div>
                        		<Button variant="danger" style={{ float: "right"}} onClick={this.deleteCompanyData}>X</Button>
                        		<div className="center_comp mb-5">
                        		    <Form>
                                      <Form.Row className="align-items-center">
                                        <Col sm={8} className="my-1">
                                          <Form.Control onChange={this.onChange}  type="text" name="company" placeholder="Enter Company Name" />
                                        </Col>
                                        <Col xs="auto" className="my-1">
                                            <Button onClick={this.searchData}>Search</Button>
                                        </Col>
                                      </Form.Row>
                                    </Form>
                        		</div>
                        			<CanvasJSChart options = {options}/>

                        			<div className="center_comp mt-5 mb-3" >
                        			    <Table style={{ width: '70%' }} striped bordered hover>
                                          <thead>
                                            <tr>
                                              <th>Year</th>
                                              <th>Average</th>
                                              <th>Max</th>
                                              <th>Min</th>
                                              <th>Number of Data</th>
                                            </tr>
                                          </thead>
                                          <tbody>
                                            <tr>
                                              <td>Total</td>
                                              <td>$ {this.state.total_ave}</td>
                                              <td>$ {this.state.total_max}</td>
                                              <td>$ {this.state.total_min}</td>
                                              <td>{this.state.total_count}  (Year N/A: {this.state.total_count - this.state.fre_count - this.state.sop_count - this.state.jun_count - this.state.sen_count}) </td>
                                            </tr>
                                            <tr>
                                              <td>Freshmen</td>
                                              <td>$ {this.state.fre_ave}</td>
                                              <td>$ {this.state.fre_max}</td>
                                              <td>$ {this.state.fre_min}</td>
                                              <td>{this.state.fre_count}</td>
                                            </tr>
                                            <tr>
                                              <td>Sophomore</td>
                                              <td>$ {this.state.sop_ave}</td>
                                              <td>$ {this.state.sop_max}</td>
                                              <td>$ {this.state.sop_min}</td>
                                              <td>{this.state.sop_count}</td>
                                            </tr>
                                            <tr>
                                              <td>Junior</td>
                                              <td>$ {this.state.jun_ave}</td>
                                              <td>$ {this.state.jun_max}</td>
                                              <td>$ {this.state.jun_min}</td>
                                              <td>{this.state.jun_count}</td>
                                            </tr>
                                            <tr>
                                              <td>Senior</td>
                                              <td>$ {this.state.sen_ave}</td>
                                              <td>$ {this.state.sen_max}</td>
                                              <td>$ {this.state.sen_min}</td>
                                              <td>{this.state.sen_count}</td>
                                            </tr>
                                          </tbody>
                                        </Table>
                        			</div>

                        			<div className="center_comp mb-3">
                        			    <Card style={{ width: '70%' }}>
                        			      <Card.Header><h3 className="text-center">Office Locations</h3></Card.Header>
                                          <Card.Body>
                                            <Card.Text>
                                              {
                                                  this.state.locations.map( city => {
                                                      return <h5 className="horizontal"><Badge variant="Light">{city}</Badge></h5>
                                              })}
                                            </Card.Text>
                                          </Card.Body>
                                        </Card>
                                    </div>
                        		</div>

                </Card.Body>
           </Card>




    		);
    	}
}

export default CompanyData;
