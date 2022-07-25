<template>
  <section class="section">
    <div class="columns">
      <div class="column is-one-quarter has-text-left">
        <p class="title is-3">Register</p>
        <div class="field">
          <div class="label">Username</div>
          <div class="control">
            <input class="input" type="text" v-model="account" />
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
import { register } from "@/request/api/register";
export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: "Register",
  data() {
    return {
      account: "",
      password: "",
      email: "",
    };
  },
  methods: {
    onSubmit() {
      register(this.account, this.password, this.email)
        .then((response) => {
          console.log("correct: %o", response);
        })
        .catch((error) => {
          console.log("err: %o", error.response);
        });
    },
  },
};
</script>
