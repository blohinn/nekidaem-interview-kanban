<template>
  <div id="app">

    <router-view/>

  </div>
</template>

<script>
  export default {
    name: 'App',
    created() {
      if (this.$cookies.get("accessToken")) {
        this.$store.commit("setAccessToken", this.$cookies.get("accessToken"));
        console.log("AccessToken loaded.");
      }
    }
  }
</script>

<style>
</style>
