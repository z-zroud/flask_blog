<template>
  <section class="section">
    <div class="columns">
      <div class="column is-one-quarter has-text-left">
        <p class="title is-3">Sign In</p>
        <div class="field">
          <div class="label">Username</div>
          <div class="control">
            <input class="input" type="text" />
          </div>
        </div>
        <div class="field">
          <div class="label">Password</div>
          <div class="control">
            <input class="input" type="password" />
          </div>
        </div>

        <div class="field">
          <div class="control">
            <button class="button is-link" @click="onSubmit">Sign in</button>
          </div>
        </div>

        <br />
        <p>
          New User? <router-link to="/register">Click to Register!</router-link>
        </p>
        <p>
          Forgot Your Password?
          <a href="#">Click to Reset It</a>
        </p>
      </div>
    </div>
  </section>
</template>

<script>
import { login } from "@/request/api/login";
import { setToken } from "@/request/token";
export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: "Login",
  data() {
    return {
      username: "",
      password: "",
    };
  },
  methods: {
    onSubmit() {
      login(this.username, this.password)
        .then((response) => {
          setToken(response.data.token);
        })
        .catch((error) => {
          console.log(error.response);
        });
    },
  },
};
</script>
