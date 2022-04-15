import React from 'react'

class TodoForm extends React.Component {
    constructor(props) {
        console.log(props)
        super(props)
        this.state = {content: '',
                      project: props.projects[0].uid
        }
    }

    handleChange(event) {
        console.log(event.target.name)
        console.log(event.target.value)
        this.setState(
            {
                [event.target.name]: event.target.value
            }
            )
    }

    handleSubmit(event) {
        console.log(this.state.content)
        console.log(this.state.project)

        this.props.createTodo(this.state.content, this.state.project)
        event.preventDefault()
    }

    render() {
        return (
            <form onSubmit={(event) => this.handleSubmit(event)}>
                <div className="form-group">
                    <label htmlfor="content">Заметка</label>
                    <textarea type="text" className="form-control" rows='5'  name="content"
                           value={this.state.content} onChange={(event) => this.handleChange(event)}/>
                </div>
                <div className="form-group">
                    <label htmlFor="project">Проект</label>
                    <select name="project" className='form-control'
                            onChange={(event)=>this.handleChange(event)}>
                            {this.props.projects.map((item)=><option value={item.uid}>{item.title}</option>)}
                    </select>
                </div>
                <input type="submit" className="btn btn-primary" value="Сохранить"/>
            </form>
        );
    }
}

export default TodoForm