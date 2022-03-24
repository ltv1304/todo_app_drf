import React, {Component} from 'react';
import './service_users.css';
import ApiClient from '../../services/ApiClient'

const ServiceUserItem = ({user}) => {

    const {uid, userName, firstName, lastName, email} = user;
    
    return(
        <tr key={uid}>
            <td>
                {userName}
            </td>
            <td>
                {firstName}
            </td>
            <td>
                {lastName}
            </td>
            <td>
                {email}
            </td>
        </tr>
    )
}

export default class ServiceUsersList extends Component {

    apiClient = new ApiClient()

    state = {
        users: []
    }

    componentDidMount() {
        this.apiClient.getAllServiceUsers()
            .then(response => {
                const users = response.data.results
                console.log(users)
                this.setState(
                    {
                        'users': users
                    }
                )
            })
    }


    render() {
    return (
        <table className="table">
            <thead>
                <tr>
                    <th>Псевдоним</th>
                    <th>Имя</th>
                    <th>Фамилия</th>
                    <th>email</th>
                </tr>
            </thead>
            <tbody>
                {this.state.users.map((user) => <ServiceUserItem user={user} />)}
            </tbody>
        </table>
    )
    }
}
