import axios from 'axios';
// import authHeader from './auth-header';


class UserService {
  getAllAgents() {
    return axios.get('/agents');
  }


}

export default new UserService();
