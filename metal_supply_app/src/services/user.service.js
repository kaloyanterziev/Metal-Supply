import axios from 'axios';
import authHeader from './auth-header';


class UserService {
  getAllAgents() {
    return axios.get('/agents');
  }

  getAgent(id) {
    return axios.get('/agents/' + id);
  }

  getAgentRecords() {
    return axios.get('/agents/records',
        { headers: authHeader() });
  }

}

export default new UserService();
