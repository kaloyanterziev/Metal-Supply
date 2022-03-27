export default function authHeader() {
  let user = JSON.parse(localStorage.getItem('user'));
  if (user && user.authorization) {
    return { Authorization: 'Bearer ' + user.authorization }; // for Spring Boot back-end
    // return { 'x-access-token': user.accessToken };       // for Node.js Express back-end
  } else {
    return {};
  }
}
