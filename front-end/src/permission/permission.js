import router from "@/router/index";

let token = sessionStorage.getItem("token");

router.beforeEach((to, from, next) => {
  if (to.meta.token) {
    if (token) {
      next();
    } else {
      next({
        path: "/login",
      });
    }
  } else {
    next();
  }
});
