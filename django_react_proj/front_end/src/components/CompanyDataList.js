import React, {Component} from 'react';
import CompanyData from './CompanyData';
import {Button, Card} from 'react-bootstrap';

class CompanyDataList extends Component{

    state = {
        companyDataList :[<CompanyData />]
    }

    addCompanyData = () => {
        let newList =  this.state.companyDataList.concat(<CompanyData />);
        this.setState({companyDataList : newList});
        console.log(this.state.companyDataList)
    }

    render(){
        return(
            <div>
                <h1 className="text-center">Company Data</h1>

                    {
                        this.state.companyDataList.map( (companyData) => {
                            return <div>{companyData}</div>
                        })
                    }

                <div className="center_comp">
                    <Button className="mb-3" onClick={this.addCompanyData}>Add Another Company</Button>
                </div>

            </div>
        );
    }
}
export default CompanyDataList;
