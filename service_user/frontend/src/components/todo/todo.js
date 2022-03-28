import React from 'react';
import './todo.css';

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

const ToDosList = ({todos}) => {
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
                {todos.map((todo) => <ToDoItem todo={todo}/>)}
                </tbody>
            </table>
        )
}

export default ToDosList