import React from 'react';
import './todo.css';
import {Link} from "react-router-dom";

const ToDoItem = ({todo, usersList, projectList, deleteTodo}) => {
    const {uid, content, project, user, activeFlag} = todo;
    return(
        <tr key={uid}>
            <td>
                {content}
            </td>
            <td>
                {projectList.find(el => el.uid == project).title}
            </td>
            <td>
                {usersList.find(el => el.uid == user).username}
            </td>
            <td>
                {activeFlag ? 'Актуально' : 'Некатуально'}
            </td>
            <td>
                {activeFlag ?
                    <button onClick={()=>deleteTodo(uid)} type='button'>
                        <span className="glyphicon glyphicon-trash" aria-hidden="true"></span>
                    </button>
                    : ''}
            </td>
        </tr>
    )
}

const ToDosList = ({todos, users, projects, deleteTodo}) => {
        return (
            <div>
                <table className="table">
                    <thead>
                    <tr>
                        <th>Заметка</th>
                        <th>Проект</th>
                        <th>Пользователь</th>
                        <th>Состояние</th>
                        <th></th>
                    </tr>
                    </thead>
                    <tbody>
                    {todos.map((todo) => <ToDoItem todo={todo}
                                                   usersList={users}
                                                   projectList={projects}
                                                   deleteTodo={deleteTodo}/>)}
                    </tbody>
                </table>
                <hr></hr>
                <div className='text-center'>
                    <Link to='/todos/create'>
                        <button className='btn btn-primary btn-lg' type="button">
                            Добавить заметку
                        </button>
                    </Link>
                </div>
            </div>
        )
}

export default ToDosList