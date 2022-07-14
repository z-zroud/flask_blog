import axios from "axios";
import { getToken } from "@/request/token";

let service = axios.create({
  baseURL: "http://localhost:5000/api/",
  timeout: 6000,
});

//请求拦截
service.interceptors.request.use(
  (config) => {
    if (getToken()) {
      config.headers["token"] = getToken();
    }
    return config;
  },
  (err) => {
    return Promise.reject(err);
  }
);

//响应拦截
service.interceptors.response.use(
  (response) => {
    let resp = response.data;
    if (resp.code == "401") {
      location.href = "login";
    }
    return Promise.resolve(resp);
  },
  (err) => {
    return Promise.reject(err);
  }
);

export default service;
