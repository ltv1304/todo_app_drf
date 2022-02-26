import React from 'react'


const ServiceUserItem = ({user}) => {
    return(
        <tr key={user.email}>
            <td>
                {user.firstname}
            </td>
            <td>
                {user.lastname}
            </td>
            <td>
                {user.email}
            </td>
        </tr>
    )
}

const ServiceUsersList = ({users}) => {
    return (
        <table>
            <thead>
                <tr>
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
