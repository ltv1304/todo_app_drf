import React from 'react';
import './service_users.css';

const ServiceUserItem = ({user}) => {

    const {uid, username, firstName, lastName, email} = user;
    
    return(
        <tr key={uid}>
            <td>
                {username}
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

const ServiceUsersList = ({users}) => {
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
                {users.map((user) => <ServiceUserItem user={user} />)}
            </tbody>
        </table>
    )
}

export default ServiceUsersList