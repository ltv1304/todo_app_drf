import React from 'react'
import axios from 'axios'
import ServiceUsersList from './components/service_users.js'


class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'service_users': []
        }
    }
    
    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/service_user/')
            .then(response => {
                const service_users = response.data
                this.setState(
                    {
                        'service_users': service_users
                    }
                )
            }).catch(error => console.log(error))
    }

    render () {
        return (
            <div>
                <ServiceUsersList users={this.state.service_users} />
            </div>
        )
    }
}

export default App;
