<template>
  <div class="notification" :class="[alertType]">
    {{ message }}
  </div>
</template>

<script>
export default {
  props: ["alertType", "message"],
};
</script>
