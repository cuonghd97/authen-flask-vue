<template>
  <form>
    <label for="fullname">Fullname</label>
    <div>
      <input type="text" id="fullame" v-model="fullname" required autofocus>
    </div>

    <label for="username">Username</label>
    <div>
      <input type="text" id="username" v-model="username" required>
    </div>

    <label for="password">Password</label>
    <div>
      <input type="password" id="password" v-model="password" required>
    </div>

    <div>
      <button type="submit" v-on:click="handleSubmit">Register</button>
    </div>
  </form>
</template>
<script>
export default {
  props: ["nextUrl"],
  data: function() {
    return {
      fullname: "",
      username: "",
      password: ""
    };
  },
  methods: {
    handleSubmit: function(e) {
      e.preventDefault();
      const url = "http://localhost:5000/register";
      if (this.fullname && this.username && this.password) {
        this.$http
          .post(url, {
            fullname: this.fullname,
            username: this.username,
            password: this.password
          })
          .then(function(res) {
            console.log(res);
            localStorage.setItem("jwt", res.data.access_token);
            if (localStorage.getItem("jwt") != null) {
              this.$emit("loggedIn");
              this.$router.push("dashboard")
              // if (this.$route.params.nextUrl != null) {
                // this.$router.push(this.$route.params.nextUrl);
              // } else {
                // this.$router.push("/");
              // }
            }
          });
      }
    }
  }
};
</script>
