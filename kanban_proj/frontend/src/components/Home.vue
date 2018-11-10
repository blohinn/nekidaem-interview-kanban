<template>
  <div id="home">
    <div class="row">
      <div class="col-6 mx-auto">


        <div class="card auth-card">
          <div class="card-body text-center">
            <h3>Simple kanban app</h3>
            <br>

            <a v-bind:href="authUri" class="btn btn-primary btn-lg active" role="button" aria-pressed="true">
              Auth and see my boards
            </a>

          </div>
        </div>

      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'Home',
    data() {
      return {
        msg: 'Welcome to Your Vue.js App'
      }
    },
    computed: {
      authUri() {

        let redirect_uri = '';

        if (process.env.NODE_ENV === 'development') {
          redirect_uri = 'http://localhost:8080/receive-token'
        } else {
          redirect_uri = window.location.protocol + '//' + window.location.hostname + '/receive-token'
        }

        console.log(redirect_uri);

        let uri = `${process.env.API_URL}/oauth/authorize?client_id=${process.env.API_APP_ID}&response_type=token&redirect_uri=${redirect_uri}`;

        console.log(uri);
        return uri;
      }
    }
  }
</script>


<style scoped>
  .auth-card {
    margin-top: 10%;
  }
</style>
