import service from "./service";

export function requestPost(url, data) {
  let config = arguments[2] ? arguments[2] : {};
  return service.post(url, data, config);
}
