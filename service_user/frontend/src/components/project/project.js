import React, {Component} from 'react';
import './project.css';
import ApiClient from "../../services/ApiClient";
import {Link} from 'react-router-dom'

const ProjectItem = ({project}) => {
    
    const {uid, title, path, users} = project;
    
    return(
        <tr key={uid}>
            <td>
                <Link to={`project/${uid}`}>{title}</Link>
            </td>
            <td>
                {path}
            </td>
            <td>
                {users}
            </td>
        </tr>
    )
}

export default class ProjectsList extends Component {
    apiClient = new ApiClient()

    state = {
        projects: []
    }

    componentDidMount() {
        this.apiClient.getAllProjects()
            .then(response => {
                const projects = response.data.results
                this.setState(
                    {
                        'projects': projects
                    }
                )
            })
    }

    render() {
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
                {this.state.projects.map((project) => <ProjectItem project={project}/>)}
                </tbody>
            </table>
        )
    }
}