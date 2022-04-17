import React from 'react'

class ProjectForm extends React.Component {
    constructor(props) {
        super(props)
        this.state = {title: '',
                      path: '',
                      users:[]}
    }

    handleChange(event) {
        console.log(event.target.name)
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
        this.props.createProject(this.state.title, this.state.path, this.state.users)
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
                            onChange={(event)=>this.handleChange(event)} multiple>
                            {this.props.users.map((item)=><option value={item.uid}>{item.username}</option>)}
                    </select>
                </div>
                <input type="submit" className="btn btn-primary" value="Сохранить"/>
            </form>
        );
    }
}

export default ProjectForm