import { requestPost } from "../common";
// const server = "http://localhost:5000/api/users";
export function register(account, password, email) {
  const url = "users";
  let data = {
    account,
    password,
    email,
  };

  return requestPost(url, data);
}
