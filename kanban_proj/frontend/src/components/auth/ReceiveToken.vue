<template>
  <div id="receive-token">
    <div class="container-fluid">
      <div class="row">
        <div class="col-12">
          <br>
          <template v-if="accessTokenReceived">
            <h1>Auth...</h1>
            <p>You will be redirected to home page automatically.</p>
          </template>

          <template v-if="accessToken">
            <h1>You already authorized.</h1>
            <a href="/">Back to home page.</a>
          </template>

          <template v-if="!accessToken && !accessTokenReceived">
            <h1>Error while auth.</h1>
            <a href="/">Back to home page and try again.</a>
          </template>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: "ReceiveToken",
    data() {
      return {
        accessTokenReceived: false
      };
    },
    computed: {
      accessToken() {
        return this.$store.state.accessToken;
      }
    },
    created() {
      let url_after_sharp = window.location.hash.substr(1);
      let accessToken = url_after_sharp.split("&")[0].split("=")[1];

      // По хорошему - здесь бы не мешало получить по токену информацию о пользователе,
      // чтобы убедиться, что токен действительный.

      if (accessToken) {
        this.accessTokenReceived = true;
        this.$cookies.set("accessToken", accessToken, {expires: 365});
        window.location.replace("/");
      }
    }
  }
</script>

<style scoped>

</style>
