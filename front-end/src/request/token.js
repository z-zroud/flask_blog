export function getToken() {
  return window.localStorage.getItem("token");
}

export function setToken(token) {
  window.localStorage.setItem("blog-token", token);
}
