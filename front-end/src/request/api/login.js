import { requestPost } from "../common";

export function login(username, password) {
  const url = "login";
  let config = {
    auth: {
      username: username,
      password: password,
    },
  };

  return requestPost(url, {}, config);
}
