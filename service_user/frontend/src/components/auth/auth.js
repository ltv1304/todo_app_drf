import React from 'react'

class LoginForm extends React.Component {
    constructor(props) {
        super(props)
        this.state = {login: '', password: ''}
    }

    handleChange(event) {
        this.setState(
            {
                [event.target.name]: event.target.value
            }
        );
    }

    handleSubmit(event) {
        this.props.get_token(this.state.login, this.state.password)
        console.log(this.state.login + ' ' + this.state.password)
        event.preventDefault()
    }

    render() {
        return (
            <form id="signin" className="form-inline text-center" onSubmit={(event) => this.handleSubmit(event)}>
                <input type="text" name="login" className="form-control" id="signin-email" placeholder="User name"
                       value={this.state.login} onChange={(event) => this.handleChange(event)}/>
                <input type="password" name="password" className="form-control" id="signin-password" placeholder="Password"
                       value={this.state.password} onChange={(event) => this.handleChange(event)}/>
                <button type="submit" className="btn btn-default">Sign in</button>
            </form>
        );
    }
}

export default LoginForm