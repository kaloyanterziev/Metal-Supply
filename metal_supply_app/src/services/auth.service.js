import axios from 'axios';

class AuthService {
  login(user) {
    return axios
      .post('/authentication', {
        email: user.email,
        password: user.password
      })
      .then(response => {
        if (response.data.accessToken) {
          localStorage.setItem('user', JSON.stringify(response.data));
        }

        return response.data;
      });
  }

  logout() {
    localStorage.removeItem('user');
  }

  register(user) {
    return axios.post('/agents', {
      name: user.name,
      email: user.email,
      password: user.password,
      role: parseInt(user.role)
    });
  }
}

export default new AuthService();
