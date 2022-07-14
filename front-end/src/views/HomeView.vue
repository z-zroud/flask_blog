<template>
  <div class="home">
    <Ping msg="Welcome to Your Vue.js App" />
  </div>
</template>

<script>
// @ is an alias to /src
import Ping from "@/components/Ping.vue";

export default {
  name: "HomeView",
  components: {
    Ping,
  },
};
</script>
