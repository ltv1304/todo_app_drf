import React from 'react'

class ProjectUpdateForm extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            uid: this.props.location.project.uid,
            title: this.props.location.project.title,
            path: this.props.location.project.path,
            users: this.props.location.project.users,
            all_users: this.props.location.usersList
        }
    }

    handleChange(event) {
        if (event.target.name == 'users'){
            let target = event.target
		    let name = target.name
            let value = Array.from(target.selectedOptions, option => option.value);
            this.setState({
                [name]: value
            });
        } else {
            this.setState(
                {
                    [event.target.name]: event.target.value
                }
            );
        }
    }

    handleSubmit(event) {
        this.props.location.updateProject(this.state.uid, this.state.title, this.state.path, this.state.users)
        event.preventDefault()
    }
    render() {
        return (
            <form onSubmit={(event) => this.handleSubmit(event)}>
                <div className="form-group">
                    <label htmlfor="title">Название проекта</label>
                    <input type="text" className="form-control" name="title"
                           value={this.state.title} onChange={(event) => this.handleChange(event)}/>
                </div>
                <div className="form-group">
                    <label htmlfor="path">Путь к проекту</label>
                    <input type="text" className="form-control" name="path"
                           value={this.state.path} onChange={(event) => this.handleChange(event)}/>
                </div>
                <div className="form-group">
                    <label htmlFor="users">Пользователи проекта</label>
                    <select name="users" className='form-control'
                            onChange={(event)=>this.handleChange(event)}
                            value={this.state.users}
                            multiple>
                            {this.state.all_users.map((item)=><option value={item.uid}>{item.username}</option>)}
                    </select>
                </div>
                <input type="submit" className="btn btn-primary" value="Обновить"/>
            </form>
        );
    }
}

export default ProjectUpdateForm