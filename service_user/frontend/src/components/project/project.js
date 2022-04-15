import React from 'react';
import './project.css';
import {Link} from 'react-router-dom'

const ProjectItem = ({project, usersList, deleteProject, updateProject}) => {

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
                <ul>
                    {usersList.filter((item) => users.includes(item.uid)).map((item)=><li>{item.username}</li>)}
                </ul>
            </td>
            <td>
                <span>
                    <button onClick={()=>deleteProject(uid)} type='button'>
                        <span className="glyphicon glyphicon-trash" aria-hidden="true"></span>
                    </button>
                    <Link to={{ pathname: "/projects/update",
                                project: project,
                                usersList: [...usersList],
                                updateProject: updateProject
                            }}>
                        <button type='button'>
                        <span className="glyphicon glyphicon-pencil" aria-hidden="true"></span>
                        </button>
                    </Link>
                </span>
            </td>
        </tr>
    )
}

class ProjectsList extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            projects:this.props.projects
        }
    }

    handleChange(event) {
        console.log(event.target.value)
        let value = this.props.projects.filter((item) => item.title.includes(event.target.value))
        this.setState(
            {
                projects: value
            }
            )
    }


    render() {
        const {users} = this.props
        return (
            <div>
                <input type="text" className="form-control" placeholder='поиск...' onChange={(event)=>this.handleChange(event)}/>
                <hr></hr>
                <table className="table">
                    <thead>
                    <tr>
                        <th>Название</th>
                        <th>Адрес</th>
                        <th>Пользователи</th>
                        <th></th>
                    </tr>
                    </thead>
                    <tbody>
                    {this.state.projects.map((project) => <ProjectItem project={project}
                                                                           usersList={users}
                                                                           deleteProject={this.props.deleteProject}
                                                                           updateProject={this.props.updateProject}/>)}
                    </tbody>
                </table>
                <hr></hr>
                <div className='text-center'>
                    <Link to='/projects/create'>
                        <button className='btn btn-primary btn-lg' type="button">
                            Добавить проект
                        </button>
                    </Link>
                </div>
            </div>
        )
    }
}

export default ProjectsList