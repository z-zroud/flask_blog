<template>
  <section class="section">
    <div class="columns">
      <div class="column is-one-quarter has-text-left">
        <p class="title is-3">Register</p>
        <div class="field">
          <div class="label">Username</div>
          <div class="control has-icons-left has-icons-right">
            <input class="input" name="field" type="text" v-model="value" />
            <span class="icon is-small is-left">
              <i class="fas fa-user"></i>
            </span>
            <span class="icon is-small is-right">
              <i class="fas fa-check"></i>
            </span>
          </div>
          <span>{{ errorMessage }}</span>
        </div>
        <div class="field">
          <div class="label">Email address</div>
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
            <button class="button is-link" @click="onSubmit">Register</button>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import { register } from "@/request/api/register";
import { useField } from "vee-validate";

export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: "Register",

  setup() {
    // Validator function
    const isRequired = (value) => (value ? true : "This field is required");
    const { value, errorMessage } = useField("field", isRequired);

    return {
      value,
      errorMessage,
    };
  },
  data() {
    return {
      account: "",
      password: "",
      email: "",
    };
  },
  methods: {
    isRequired(value) {
      return value ? true : "This field is required";
    },
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
