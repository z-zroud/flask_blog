export function getToken() {
  return window.localStorage.getItem("blog-token");
}

export function setToken(token) {
  window.localStorage.setItem("blog-token", token);
}
