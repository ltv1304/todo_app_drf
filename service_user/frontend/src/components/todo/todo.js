import React, {Component} from 'react';
import './todo.css';
import ApiClient from "../../services/ApiClient";

const ToDoItem = ({todo}) => {
    const {url, content, project, user, activeFlag} = todo;
    
    return(
        <tr key={url}>
            <td>
                {content}
            </td>
            <td>
                {project}
            </td>
            <td>
                {user}
            </td>
            <td>
                {activeFlag}
            </td>
        </tr>
    )
}

export default class ToDosList extends Component {
    apiClient = new ApiClient()

    state = {
        todos: []
    }

    componentDidMount() {
        this.apiClient.getAllToDos()
            .then(response => {
                const todos = response.data.results
                this.setState(
                    {
                        'todos': todos
                    }
                )
            })
    }

    render() {
        return (
            <table className="table">
                <thead>
                <tr>
                    <th>Заметка</th>
                    <th>Проект</th>
                    <th>Пользователь</th>
                    <th>Состояние</th>
                </tr>
                </thead>
                <tbody>
                {this.state.todos.map((todo) => <ToDoItem todo={todo}/>)}
                </tbody>
            </table>
        )
    }
}