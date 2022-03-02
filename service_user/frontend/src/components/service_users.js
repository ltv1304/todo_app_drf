import React from 'react';
import './service_users.css';

const ServiceUserItem = ({user}) => {
    
    const {username, firstname, lastname, email} = user;
    
    return(
        <tr key={username}>
            <td>
                {username}
            </td>
            <td>
                {firstname}
            </td>
            <td>
                {lastname}
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
