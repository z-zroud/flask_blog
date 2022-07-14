import { createRouter, createWebHistory } from "vue-router";

function importRouters(r) {
  let routers = [];
  r.keys().forEach((item) => {
    routers.push(r(item).default);
  });
  console.info(routers);
  return routers;
}

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes: importRouters(require.context("./", true, /\.router\.js/)),
});

export default router;
