import React from 'react';
import SignUp from './SignUp'
import { BrowserRouter as Router } from 'react-router-dom';
import Route from 'react-router-dom/Route';
import './App.css';

class App extends React.Component {
    render() {
        return (
            <Router>
                <Route exact path="/" render = { () => <SignUp /> } 
                />
                <Route exact path="/:userId" 
                    render = { (props) => <SignUp userId={props.match.params.userId}/>}
                />
            </Router>
            )
    }
}
export default App;
