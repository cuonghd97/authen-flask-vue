<template>
  <div>
    <h3>Dashboard</h3>
    <a href="#" v-on:click="logoutAccess">Logout</a>
  </div>
</template>
<script>
export default {
  methods: {
    logoutAccess: function(e) {
      e.preventDefault();
      const token = localStorage.getItem("jwt");
      console.log(token);
      const url = "http://localhost:5000/logout/access";
      this.$http
        .post(url, {
          headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${token}`
          }
        })
        .then(res => {
          console.log(res);
          this.$router.push("login");
        });
    }
  }
};
</script>
