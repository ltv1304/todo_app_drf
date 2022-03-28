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

    getAllServiceUsers(headers) {
        return this.getData('api/users/service_user/', headers)
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

}

export default ApiClient