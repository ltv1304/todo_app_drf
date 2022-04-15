import React from 'react';
import './projectDetail.css';
import {useParams} from "react-router-dom";



const ProjectDetail = ({users, todos, projects}) => {
    let {uid}  = useParams();
    let thisProject =  projects.find(el => el.uid == uid)
    let thisUsers = users.filter(el => thisProject.users.includes(el.uid))
    let thisTodos = todos.filter(el => el.project == uid)

    console.log(thisTodos)
    return (
        <>
            <h1 className="text-center">Название проекта: {thisProject.title}</h1>
            <p>Над проектом трудятся:</p>
            <ul>
                {thisUsers.map((item)=><li>{item.username}</li>)}
            </ul>
            <hr></hr>
            <h3 className="text-center">Заметки проекта</h3>
            <ul>
                {thisTodos.map((item)=> item.activeFlag ? <li>{item.content} by {users.find(el => el.uid == item.user).username}</li> :
                                                           <li><s>{item.content}</s> by {users.find(el => el.uid == item.user).username}</li> )}
            </ul>
        </>

    )
}

export default ProjectDetail