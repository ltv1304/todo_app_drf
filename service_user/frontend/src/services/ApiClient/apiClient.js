import axios from 'axios'

class ApiClient {

    baseAddr = 'http://localhost:8000/';

    async getData(url, headers) {
        const data = await axios.get(`${this.baseAddr}${url}`, {headers});
        return await data;
    }

    async tokenRequest(auth_data) {
        const data = await axios.post(`${this.baseAddr}api-token-auth/`, auth_data);
        return await data;
    }

    async deleteItem(url, headers) {
        const data = await axios.delete(`${this.baseAddr}${url}`, {headers});
        return await data;
    }

    async createItem(url, new_data, headers) {
        const data = await axios.post(`${this.baseAddr}${url}`, new_data, {headers});
        return await data;
    }

    async updateItem(url, new_data, headers) {
        const data = await axios.put(`${this.baseAddr}${url}`, new_data, {headers});
        return await data;
    }

    getAllServiceUsers(headers) {
        return this.getData('api/users/v1/service_user/', headers)
    }

    getAllToDos(headers) {
        return this.getData('api/todos/todo/', headers)
    }

    getAllProjects(headers) {
        return this.getData('api/projects/project/', headers)
    }

    getProjectDetail(uid, headers) {
        return this.getData(`api/projects/project/${uid}/`, headers)
    }

    getToken(username, password) {
        let auth_data = {username: username, password: password}
        return this.tokenRequest(auth_data)
    }

    deleteProject(uid, headers) {
        return this.deleteItem(`api/projects/project/${uid}/`, headers)
    }

    deleteTodo(uid, headers) {
        return this.deleteItem(`api/todos/todo/${uid}/`, headers)
    }

    createProject(new_data, headers) {
        return this.createItem(`api/projects/project/`, new_data, headers)
    }

    updateProject(new_data, headers) {
        return this.updateItem(`api/projects/project/${new_data.uid}/`, new_data, headers)
    }

    createTodo(new_data, headers) {
        return this.createItem(`api/todos/todo/`, new_data, headers)
    }

}

export default ApiClient