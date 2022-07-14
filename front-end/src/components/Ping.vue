<template>
  <div class="section is-link is-fullheight-with-navbar">
    <button class="button is-primary">{{ msg }}</button>
    <button class="button is-dark">{{ msg }}</button>
  </div>
</template>

<script>
import axios from "axios";
export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: "Ping",
  data() {
    return {
      msg: "",
    };
  },
  methods: {
    getMessage() {
      const path = "http://localhost:5000/api/ping";
      axios
        .get(path)
        .then((res) => {
          this.msg = res.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  created() {
    this.getMessage();
  },
};
</script>
