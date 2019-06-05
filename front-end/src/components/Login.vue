<template>
  <form>
    <label for="username">Username</label>
    <div>
      <input type="text" id="username" v-model="username" required autofocus>
    </div>

    <label for="password">Password</label>
    <div>
      <input type="password" v-model="password" id="password">
    </div>

    <div>
      <button type="submit" v-on:click="handleSubmit">Login</button>
    </div>
  </form>
</template>
<script>
export default {
  data: function() {
    return {
      username: "",
      password: ""
    }
  },
  methods: {
    handleSubmit: function(e) {
      e.preventDefault()
      const url = "http://localhost:5000/login"
      if (this.username && this.password) {
        this.$http.post(url, {
          username: this.username,
          password: this.password
        })
        .then((res) => {
          console.log(res)
          localStorage.setItem("jwt", res.data.access_token)
          this.$emit("loggedIn")
          if (localStorage.getItem("jwt") !== null) {
            this.$router.push("dashboard")
          }
        })
        .catch(function(err) {
          console.error(err)
        })
      }
    }
  }
}
</script>
