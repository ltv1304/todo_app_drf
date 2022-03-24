import axios from 'axios'

class ApiClient {

    baseAddr = 'http://localhost:8000/api';

    async getData(url) {
        const data = await axios(`${this.baseAddr}${url}`);
        return await data;
    }

    getAllServiceUsers() {
        return this.getData('/users/service_user/')
    }

    getAllToDos() {
        return this.getData('/todos/todo/')
    }

    getAllProjects() {
        return this.getData('/projects/project/')
    }

    getProjectDetail(uid) {
        return this.getData(`/projects/project/${uid}/`)
    }

}

export default ApiClient