import React, { Component, Fragment } from "react";
import { Button, Modal, ModalHeader, ModalBody } from "reactstrap";
import NewInternForm from "./NewInternForm";

import '../App.css';

class NewStudentModal extends Component {
  state = {
    modal: false
  };

  toggle = () => {
    this.setState(previous => ({
      modal: !previous.modal
    }));
  };

  button = (
    <Button color="primary" className="float-right cm-1" onClick={this.toggle} style={{ minWidth: "200px" }}>Post Info</Button>
  );

  render() {
      const title = "Post New Info";
    
    return (
      <Fragment>
        {this.button} 
        <Modal size="lg" isOpen={this.state.modal} toggle={this.toggle}>
  
        <ModalHeader toggle={this.toggle}>{title}</ModalHeader>
          <ModalBody>
            <NewInternForm
              resetState={this.props.resetState}
              toggle={this.toggle}
            />
          </ModalBody>
        </Modal>
      </Fragment>
    );
  }
}

export default NewStudentModal;
