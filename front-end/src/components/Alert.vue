<template>
  <div class="notification" :class="[alertType]">
    {{ message }}
  </div>
</template>

<script>
export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: "Alert",
  props: ["alertType", "message"],
};
</script>
