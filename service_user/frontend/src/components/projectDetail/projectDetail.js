import React, {useEffect} from 'react';
import './projectDetail.css';
import {useParams} from "react-router-dom";
import axios from 'axios'
import ApiClient from "../../services/ApiClient";


const UserTableItem = ({user}) => {

    return(
        <tr>
            <td>
                {user}
            </td>
        </tr>
    )
}
let apiClient = new ApiClient()

const ProjectDetail = ({get_headers}) => {
    let {uid}  = useParams();
    const headers = get_headers()
    const [users, getProjectUsers] = React.useState('');

    useEffect(() => {
        apiClient.getProjectDetail(uid, headers)
            .then(response => {
                const users = response.data
                getProjectUsers(users)
            })
    }, []);

    if (users==='') return null;

    return (
        <table className="table">
            <thead>
            <tr>
                <th>Название</th>
                <th>Адрес</th>
                <th>Пользователи</th>
            </tr>
            </thead>
            <tbody>
            <tr>
                <td>{users.title}</td>
                <td>{users.path}</td>
                <td>
                    <table>
                        <tbody>
                        {users.users.map(user => <UserTableItem user={user} /> )}
                        </tbody>
                    </table>
                </td>
            </tr>
            </tbody>
        </table>
    )
}

export default ProjectDetail