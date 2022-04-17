import React from 'react'
import ServiceUsersList from '../servise_users'
import {ToDosList, TodoForm} from "../todo";
import {ProjectsList, ProjectForm} from "../project";
import ProjectDetail from "../projectDetail";
import LoginForm from "../auth";
import './App.css'
import {Link, Route, Switch} from "react-router-dom";
import ApiClient from "../../services/ApiClient";
import Cookies from "universal-cookie/lib";
import ProjectUpdateForm from "../project/projectUpdateForm";



const NotFound404 = ({location}) => {
    return (
        <div>
            <h1>Страница по адресу '{location.pathname}' не найдена</h1>
        </div>
    )
}

class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'todos': [],
            'projects': [],
            'users': [],
            'token': '',
            'username': ''
        }
    }

    set_token(token, username) {
        const cookies = new Cookies()
        cookies.set('token', token)
        this.setState({'username': username})
        this.setState({'token': token}, ()=>this.load_data())
    }

    is_authenticated() {
        // return this.state.token != ''
        return !!this.state.username
    }

    logout() {
        this.set_token('', '')
    }

    get_token_from_storage() {
        const cookies = new Cookies()
        const token = cookies.get('token')
        const username = cookies.get('username')
        this.setState({'token': token}, ()=>this.load_data())
    }

    get_token(username, password) {
        this.apiClient.getToken(username, password)
            .then(response => {
                this.set_token(response.data['token'], username)
            }).catch(error => alert('Неверный логин или пароль'))
    }

    get_headers() {
        let headers = {
            'Content-Type': 'application/json'
        }
        if (this.is_authenticated()) {
            headers['Authorization'] = 'Token ' + this.state.token
        }
        return headers
    }

    apiClient = new ApiClient()

    load_data() {
        const headers = this.get_headers()
        this.apiClient.getAllProjects(headers)
            .then(response => {
                this.setState({'projects': response.data.results})
            }).catch(error => {
            console.log(error)
            this.setState({projects: []})
        })
        this.apiClient.getAllServiceUsers(headers)
            .then(response => {
                console.log(response.data.results)
                this.setState({'users': response.data.results})
            }).catch(error => {
            console.log(error)
            this.setState({users: []})
        })
        this.apiClient.getAllToDos(headers)
            .then(response => {
                this.setState({'todos': response.data.results})
            }).catch(error => {
                this.setState({todos: []})
                console.log(error)
        })
    }

    deleteProject(uid) {
        const headers = this.get_headers()
        this.apiClient.deleteProject(uid, headers)
            .then(response => {
                this.setState({'projects': this.state.projects.filter((item) => item.uid !== uid)})
            }).catch(error => console.log(error))
    }

    createProject(title, path, users){
        const headers = this.get_headers()
        const new_data = {title: title, path: path, users:users}
        this.apiClient.createProject(new_data, headers)
            .then(response => {
                console.log(response.data)
                let new_peoject = response.data
                this.setState({projects:[...this.state.projects, new_peoject]})
            }).catch(error => {console.log(error.response.data)})
    }

    updateProject(uid, title, path, users){
        const headers = this.get_headers()
        const new_data = {uid: uid, title: title, path: path, users:users}
        this.apiClient.updateProject(new_data, headers)
            .then(response => {
                let updted_project = response.data
                let newProjectsList = this.state.projects.filter((item) => item.uid !== uid)
                this.setState({'projects': [...newProjectsList, updted_project]})
            }).catch(error => {console.log(error.response.data)})
    }

    createTodo(content, project){
        const headers = this.get_headers()
        const new_data = {content: content, project: project}
        this.apiClient.createTodo(new_data, headers)
            .then(response => {
                let new_todo = response.data
                this.setState({todos:[...this.state.todos, new_todo]})
            }).catch(error => {console.log(error.response.data)})
    }


    deleteTodo(uid) {
        const headers = this.get_headers()
        this.apiClient.deleteTodo(uid, headers)
            .then(response => {
                let deleted_todo = response.data
                let newTodoList = this.state.todos.filter((item) => item.uid !== uid)
                this.setState({'todos': [...newTodoList, deleted_todo]})
            }).catch(error => console.log(error))
    }

    componentDidMount() {
        this.get_token_from_storage()
    }
    render () {
        return (
            <div id="main">
                <nav className="navbar navbar-default navbar-fixed-top">
                    <div className="container">
                        <div className="navbar-header">
                            <a className="logo-font" href="#">
                                Todo
                            </a>
                        </div>
                        <div id="nav-menu" className="collapse navbar-collapse">
                            <ul className="nav navbar-nav">
                                <li>
                                    <Link to='/users'>
                                        <span className="glyphicon glyphicon-user glyph_margin" aria-hidden="true"></span>
                                        Пользователи
                                    </Link>
                                </li>
                                <li>
                                    <Link to='/projects'>
                                        <span className="glyphicon glyphicon-file glyph_margin" aria-hidden="true"></span>
                                        Проекты
                                    </Link>
                                </li>
                                <li>
                                    <Link to='/todos'>
                                        <span className="glyphicon glyphicon-envelope glyph_margin" aria-hidden="true"></span>
                                        Заметки
                                    </Link>
                                </li>
                            </ul>
                            {this.is_authenticated() ? <div id="nav-options" className="btn-group pull-right">
                                <button type="button" className="btn btn-default dropdown-toggle"
                                        data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                    {this.state.username}
                                </button>
                                <ul className="dropdown-menu">
                                    <li><a href="#" onClick={()=>this.logout()}>Logout</a></li>
                                </ul>
                            </div> : <LoginForm get_token={(username, password) => this.get_token(username, password)}/>}
                        </div>
                    </div>
                </nav>
                <section id="intro-header">
                    <div className="container">
                        <div className="row">
                            <div className="wrap-headline">
                                <h1 className="text-center">Todo app</h1>
                                <h2 className="text-center">remember you thinks</h2>
                                <hr></hr>
                            </div>
                        </div>
                    </div>
                </section>
                <div className="container">
                    <Switch>
                        <Route exact path='/' component={() => <ServiceUsersList users={this.state.users}/>}/>
                        <Route exact path='/users' component={() =><ServiceUsersList users={this.state.users}/>}/>
                        <Route exact path='/todos' component={() =><ToDosList todos={this.state.todos}
                                                                              users={this.state.users}
                                                                              projects={this.state.projects}
                                                                              deleteTodo={(uid)=>this.deleteTodo(uid)}/>}/>
                        <Route exact path='/projects' component={() =><ProjectsList projects={this.state.projects}
                                                                                    users={this.state.users}
                                                                                    deleteProject={(uid)=>this.deleteProject(uid)}
                                                                                    updateProject={(uid, title, path, users)=>this.updateProject(uid, title, path, users)}/>}/>
                        <Route exact path='/projects/create' component={() =><ProjectForm
                                    users={this.state.users}
                                    createProject={(title, path, users) => this.createProject(title, path, users)}/>}/>
                        <Route exact path='/todos/create' component={() =><TodoForm
                                    projects={this.state.projects}
                                    createTodo={(content, project) => this.createTodo(content, project)}/>}/>
                        <Route exact path='/projects/update' component={ProjectUpdateForm}/>
                        <Route path="/project/:uid">
                            <ProjectDetail users={this.state.users} todos={this.state.todos} projects={this.state.projects}/>
                        </Route>
                        <Route component={NotFound404} />
                    </Switch>
                </div>
            </div>
        )
    }
}
export default App;
