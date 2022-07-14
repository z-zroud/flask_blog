<template>
  <section class="section">
    <div class="columns">
      <div class="column is-one-quarter has-text-left">
        <p class="title is-3">Register</p>
        <div class="field">
          <div class="label">Username</div>
          <div class="control">
            <input class="input" type="text" v-model="username" />
          </div>
        </div>
        <div class="field">
          <div class="label">Email address</div>
          <div class="control">
            <input class="input" type="text" v-model="email" />
          </div>
        </div>

        <div class="field">
          <div class="label">Password</div>
          <div class="control">
            <input class="input" type="password" v-model="password" />
          </div>
        </div>

        <div class="field">
          <div class="control">
            <button class="button is-link" @click="onSubmit">Register</button>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import axios from "axios";
export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: "Login",
  data() {
    return {
      username: "",
      password: "",
      email: "",
    };
  },
  methods: {
    onSubmit() {
      const server = "http://localhost:5000/api/users";
      const user = {
        username: this.username,
        password: this.password,
        email: this.email,
      };
      axios
        .post(server, user)
        .then((response) => {
          window.localStorage.setItem("blog-token", response.data.token);
        })
        .catch((error) => {
          console.log(error.response);
        });
    },
  },
};
</script>
