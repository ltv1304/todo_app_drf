import React from 'react'
import ServiceUsersList from './components/servise_users/service_users.js'
import ToDosList from "./components/todo";
import ProjectsList from "./components/project";
import ProjectDetail from "./components/projectDetail";
import './App.css'
import {Link, Route, Switch} from "react-router-dom";

class App extends React.Component {
    render () {
        return (
        <div className="blok">
                <div className="content">
                    <header className="header">
                        <h2>To-Do App</h2>
                        <Link to='/projects'>Projects</Link>
                        <Link to='/'>Users</Link>
                        <Link to='/todos'>ToDos</Link>
                    </header>
                    <div className="table_blok container">
                        <Switch>
                            <Route exact path='/' component={ServiceUsersList} />
                            <Route exact path='/users' component={ServiceUsersList} />
                            <Route exact path='/todos' component={ToDosList} />
                            <Route exact path='/projects' component={ProjectsList} />
                            <Route path="/project/:uid">
                                <ProjectDetail />
                            </Route>
                            {/*<Route path='project/:uid' element={<ProjectDetail />} />*/}
                        </Switch>
                    </div>
                </div>
        </div>
        )
    }
}
export default App;
