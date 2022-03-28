import React from 'react';
import './project.css';
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

const ProjectsList = ({projects}) => {
        console.log(projects)
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
                {projects.map((project) => <ProjectItem project={project}/>)}
                </tbody>
            </table>
        )
}

export default ProjectsList