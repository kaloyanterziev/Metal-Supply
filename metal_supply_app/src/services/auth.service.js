import axios from 'axios';

class AuthService {
  login(user) {
    return axios
      .post('/authentication', {
        email: user.email,
        password: user.password
      })
      .then(response => {
        if (response.data.authorization) {
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
    }).then(response => {
      if (response.data.authorization) {
        delete user.password;
        user.authorization = response.data.authorization;
        user.id = response.data.id
        localStorage.setItem('user', JSON.stringify(user));
      }

      return response.data;
    });
  }
}

export default new AuthService();
