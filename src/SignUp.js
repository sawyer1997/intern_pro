import React, { Component } from "react";
export default class SignUp extends Component {

	constructor() {
        super()
        this.state = {
            firstName : "",
            lastName : "",
            email: "",
            phone: "",
            message: "",
        }
        this.baseState = this.state
        this.handleChange = this.handleChange.bind(this)
        this.handleRegister = this.handleRegister.bind(this)
        this.clearFormData = this.clearFormData.bind(this)
    }

    handleChange(event) {
        this.setState({
            [event.target.name] : event.target.value,
        })
    }

    clearFormData() {
    	console.log('Hello')
    	console.log(this.state);
    }

    handleRegister(event) {

    	event.preventDefault();

    	const data = {
    		'first_name': this.state.firstName,
    		'last_name' : this.state.lastName,
    		'email': this.state.email,
    		'phone': this.state.phone,
    		'is_referred_by': this.props.userId ? true : false,
    		'referral_id': this.props.userId ? this.props.userId : ""
    	};
    	fetch('http://127.0.0.1:8000/register/', {
    		method: 'POST',
    		headers: {
    			'Content-Type': 'application/json',
    			'Accept': 'application/json'
    		},
    		body: JSON.stringify(data)
    	})
    	.then(res => res.json())
    	.then(data => this.setState({ 
	    		message: data.message,
	    		firstName: "",
	    		lastName: "",
    		})
    	)
    	.catch(err => console.log(err))
    }

    render() {
        return (
            <form>
                <h3>Register</h3>

                <div className="form-group">
                    <label>First name</label>
                    <input 
                    	type="text"
                    	name="firstName"
                    	placeholder="First name" 
                    	onChange = {(event) => this.handleChange(event)}
                    />
                </div>

                <div className="form-group">
                    <label>Last name</label>
                    <input 
                    	type="text"
                    	name="lastName"
                    	placeholder="Last name"
                    	onChange = {(event) => this.handleChange(event)}
                    />
                </div>

                <div className="form-group">
                    <label>Email address</label>
                    <input
                    	type="email" 
                    	placeholder="Enter email" 
                    	name="email"
                    	onChange={(event) => this.handleChange(event)}
                    />
                </div>

                <div className="form-group">
                    <label>Phone number</label>
                    <input
                    	type="number" 
                    	placeholder="Enter contact number" 
                    	name="phone"
                    	onChange={(event) => this.handleChange(event)}
                    	/>
                </div>

                <button onClick={this.handleRegister}>Register</button>
                <h1>{this.state.firstName + ' ' + this.state.lastName}</h1>
                <h1>{this.state.message ? this.state.message : ''}</h1>
                <h1>{this.props.userId}</h1>
            </form>
        );
    }
}